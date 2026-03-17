from django.shortcuts import render
import json
import os

def load_data():
    """Load all data files"""
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    
    with open(os.path.join(data_dir, 'learning_paths.json')) as f:
        paths = json.load(f)
    
    with open(os.path.join(data_dir, 'job_demand.json')) as f:
        demand = json.load(f)
    
    with open(os.path.join(data_dir, 'salary_data.json')) as f:
        salaries = json.load(f)
    
    with open(os.path.join(data_dir, 'sources.json')) as f:
        sources = json.load(f)
    
    return paths, demand, salaries, sources

def home(request):
    """Home page - path and region selector"""
    paths, _, _, _ = load_data()
    
    context = {
        'paths': paths['paths'],
        'regions': ['Nigeria', 'Kenya', 'India']
    }
    return render(request, 'validator/home.html', context)

def validate_path(request):
    """Validate a learning path against job market data"""
    if request.method != 'POST':
        return home(request)
    
    learning_path = request.POST.get('learning_path')
    region = request.POST.get('region')
    
    paths, demand, salaries, sources = load_data()
    
    # Get path details
    path_obj = next((p for p in paths['paths'] if p['name'] == learning_path), None)
    
    # Get job demand for this region and path
    job_data = demand.get(region, {}).get(learning_path, {})
    salary_data = salaries.get(region, {}).get(learning_path, {})
    
    # Validation logic
    open_roles = job_data.get('open_roles', 0)
    growth = job_data.get('growth_yoy', 0)
    
    if open_roles > 300:
        validation_status = "STRONG"
        validation_color = "green"
    elif open_roles > 100:
        validation_status = "MODERATE"
        validation_color = "orange"
    else:
        validation_status = "WEAK"
        validation_color = "red"
    
    # Calculate confidence (0-100)
    confidence = min(100, (open_roles / 500) * 100 + (growth / 30) * 20)
    confidence = int(confidence)
    
    # Get alternatives (paths with more jobs)
    alternatives = []
    for path_name, path_demand in demand.get(region, {}).items():
        if path_name != learning_path:
            alternatives.append({
                'name': path_name,
                'jobs': path_demand.get('open_roles', 0),
                'growth': path_demand.get('growth_yoy', 0)
            })
    
    alternatives = sorted(alternatives, key=lambda x: x['jobs'], reverse=True)[:3]
    
    context = {
        'learning_path': learning_path,
        'region': region,
        'path_obj': path_obj,
        'validation_status': validation_status,
        'validation_color': validation_color,
        'confidence': confidence,
        'open_roles': open_roles,
        'growth': growth,
        'salary_min': salary_data.get('entry_min', 0),
        'salary_max': salary_data.get('entry_max', 0),
        'salary_currency': salary_data.get('currency', 'USD/year'),
        'sources': sources['sources'],
        'alternatives': alternatives
    }
    
    return render(request, 'validator/results.html', context)