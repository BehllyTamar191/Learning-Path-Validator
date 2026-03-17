# Model Card: Learning Path Validation Algorithm

## Algorithm Type

**Rule-Based Validation** (not machine learning)

Simple if-then logic for transparency and explainability.

## Algorithm Details

### Input Variables
- `path_name` (e.g., "Data Analytics")
- `region` (e.g., "Nigeria")
- `open_roles` = count of job postings
- `growth_yoy` = year-over-year growth %
- `salary_entry_min` = entry-level salary minimum
- `regional_median_salary` = median salary in region

### Validation Logic

```python
if open_roles > 300:
    validation = "STRONG"
    confidence = min(100, (open_roles / 500) * 100 + (growth_yoy / 30) * 20)
    
elif open_roles > 100:
    validation = "MODERATE"
    confidence = min(100, (open_roles / 300) * 60 + (growth_yoy / 25) * 30)
    
else:
    validation = "WEAK"
    confidence = min(100, (open_roles / 100) * 40 + (growth_yoy / 20) * 20)