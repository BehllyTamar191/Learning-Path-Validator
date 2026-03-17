
---

#### **SYSTEM_CARD.md**

```markdown
# System Card: Learning Path Validator

## System Overview

Learning Path Validator is a **rule-based validation system** (not machine learning) 
that matches user learning paths against regional labor market data.

## Intended Use

- Help women discover if their desired learning path has job opportunities
- Provide data-driven confidence in education decisions
- Show regional job market intelligence in an accessible format

## Who Benefits

- Women in developing regions making career decisions
- Job seekers transitioning into new fields
- Students choosing educational programs

## Who Should NOT Use This

- Career counselors making formal recommendations
- Employers making hiring decisions
- People in crisis situations (use local support services instead)

## Data Inputs

1. **User Input**: Learning path name + region
2. **Job Demand Data**: LinkedIn, Glassdoor (3-month rolling average)
3. **Salary Data**: Glassdoor, World Bank, government stats
4. **Skill Requirements**: Job descriptions (aggregated, de-identified)

## Algorithm
IF job_demand(path, region) > 300 AND salary > regional_baseline: validation = "STRONG" (80-100% confidence) ELSE IF job_demand > 100: validation = "MODERATE" (50-79% confidence) ELSE: validation = "WEAK" (validation < 50% confidence)


## Output

- Validation status (STRONG / MODERATE / WEAK)
- Confidence score (0–100%)
- Job demand (number of open roles)
- Salary range (entry-level)
- Alternative paths
- Data sources + links

## Limitations

- Data lags 1–3 months behind real-time job market
- Regional coverage limited to 3 countries initially
- Doesn't capture informal economy jobs
- Salary ranges are averages (individual outcomes vary)
- Can't predict industry disruption or sudden shifts
- Doesn't evaluate personal fit, passion, or aptitude

## Safety Considerations

### What System Does NOT Do
- Make career recommendations
- Guarantee job placement
- Evaluate individual capability
- Account for discrimination or bias in hiring
- Predict personal success

### What System DOES Do
- Show publicly available job market data
- Highlight regional demand signals
- Encourage informed decision-making
- Make reasoning transparent

### Safeguards
- Every recommendation includes data sources
- Clear disclaimer on all results
- No storage of personal data
- Regional data bias flagged explicitly
- Encourages seeking professional advice

## Bias & Fairness

### Known Biases
- Data sources may underrepresent informal economy jobs
- Salary data skews toward formal sector
- Regional data may reflect urban centers more than rural areas
- Does not account for gender pay gaps within roles

### Mitigation
- Flag limitations on every result
- Include alternative path suggestions
- Transparent about data sources
- Regular data audits for bias
- Women-centric framing (encouraging, not discouraging)

## Transparency

All recommendations show:
- ✓ Exact data sources
- ✓ Data collection date
- ✓ Confidence score
- ✓ Known limitations
- ✓ Alternative options

## Governance & Accountability

- Monthly review of job demand data
- Quarterly bias audit
- User feedback incorporated
- Open source code for external review