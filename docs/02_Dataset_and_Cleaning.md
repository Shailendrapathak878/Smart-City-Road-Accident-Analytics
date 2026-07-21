# Dataset and Data Cleaning

---

# Introduction

The Smart City Road Accident Analytics project uses a **custom synthetic road accident dataset** generated using **IRAAD (Indian Road Accident Analytics Dataset Generator)**.

Unlike publicly available datasets, the dataset used in this project has been specifically designed to simulate realistic Indian road accident scenarios while maintaining logical consistency, diversity, and analytical usefulness.

The generated dataset serves as the foundation of the complete analytics pipeline implemented in this project.

---

# About IRAAD

**IRAAD (Indian Road Accident Analytics Dataset Generator)** is a custom-built dataset generator developed to create realistic Indian road accident datasets for educational, research, and data analytics purposes.

The generator creates logically consistent accident records by combining multiple accident-related factors, including:

- Accident Information
- Driver Information
- Vehicle Information
- Road Conditions
- Weather Conditions
- Traffic Conditions
- Emergency Response
- Risk Assessment

The generated data closely resembles real-world accident scenarios while remaining completely synthetic.

---

# Dataset Information

| Property | Value |
|----------|-------|
| Dataset Generator | IRAAD |
| Dataset Type | Synthetic |
| File Format | CSV |
| Records | 50,000 |
| Columns | 61 |
| Encoding | UTF-8 |

---

# Dataset Storage

```text
data/

├── raw/
│   └── accident_dataset.csv
│
├── cleaned/
│   └── cleaned_accident_dataset.csv
│
└── featured/
    └── featured_accident_dataset.csv
```

---

# Dataset Categories

The dataset contains multiple categories of information.

## Accident Details

Includes:

- Record ID
- Accident Date
- Accident Time
- Year
- Month
- Weekday
- Hour

---

## Driver Details

Includes:

- Driver Age
- Driver Gender
- Driving Experience
- License Information

---

## Vehicle Details

Includes:

- Vehicle Type
- Vehicle Age
- Vehicle Condition
- Average Speed

---

## Road Information

Includes:

- Road Type
- Road Surface
- Road Condition
- Traffic Density

---

## Environmental Information

Includes:

- Weather
- Temperature
- Visibility
- Rainfall
- Season

---

## Emergency Information

Includes:

- Ambulance Required
- Police Required
- Estimated Response Time

---

## Risk Assessment

Includes:

- Risk Score
- Risk Level
- Risk Category

---

# Data Cleaning Overview

Raw datasets often contain inconsistencies that affect analysis quality.

To improve data quality, the project implements a complete data cleaning pipeline before performing any statistical analysis or visualization.

---

# Data Cleaning Workflow

```text
Raw Dataset
      │
      ▼
Missing Value Detection
      │
      ▼
Duplicate Detection
      │
      ▼
Business Rule Validation
      │
      ▼
Data Type Conversion
      │
      ▼
Text Standardization
      │
      ▼
Data Validation
      │
      ▼
Clean Dataset
```

---

# Missing Value Handling

The cleaning module automatically identifies missing values in the dataset.

Business rules are applied to handle missing data appropriately.

Examples include:

| Column | Cleaning Strategy |
|----------|------------------|
| estimated_response_time | Filled with 0 when emergency response is not required |
| accident_severity | Updated using business rules |
| property_damage | Updated using business rules |

After cleaning:

- Remaining Missing Values: **0**

---

# Duplicate Detection

Duplicate records are identified using Pandas.

```python
dataframe.duplicated().sum()
```

If duplicate rows exist, they are removed automatically.

Current Dataset:

- Duplicate Rows Removed: **0**

---

# Data Type Standardization

Columns are converted into appropriate data types before analysis.

Examples:

| Column | Converted To |
|----------|--------------|
| accident_datetime | datetime |
| driver_age | integer |
| average_speed | float |
| estimated_response_time | float |
| risk_score | integer |

This ensures consistent analysis and improves computational efficiency.

---

# Business Rule Validation

Several logical validation rules are applied during cleaning.

Examples include:

### Accident Severity

If an accident has not occurred, the accident severity is updated according to predefined business rules.

---

### Property Damage

Property damage information is validated based on accident occurrence.

---

### Emergency Response

If ambulance assistance is not required, the estimated response time is automatically adjusted.

These rules ensure logical consistency throughout the dataset.

---

# Text Standardization

Categorical text values are standardized by:

- Removing extra spaces
- Maintaining consistent formatting
- Normalizing text values
- Eliminating inconsistencies

This improves grouping, filtering, and visualization.

---

# Data Validation

Before proceeding to feature engineering, the cleaned dataset undergoes multiple validation checks.

Validation includes:

- Missing Value Verification
- Duplicate Verification
- Data Type Verification
- Business Rule Verification

Only validated data is used for further analysis.

---

# Clean Dataset Output

The cleaned dataset is automatically saved.

```text
data/

└── cleaned/

    └── cleaned_accident_dataset.csv
```

---

# Benefits of Data Cleaning

The cleaning process provides several advantages.

- Improved data quality
- Higher analytical accuracy
- Consistent data types
- Better statistical analysis
- More reliable visualizations
- Easier feature engineering
- Reduced data inconsistencies

---

# Summary

The Smart City Road Accident Analytics project begins with a custom synthetic dataset generated by **IRAAD (Indian Road Accident Analytics Dataset Generator)**.

A comprehensive data cleaning pipeline is then applied to transform the raw dataset into a structured, validated, and analysis-ready dataset.

The cleaning process includes missing value handling, duplicate removal, business rule validation, data type conversion, text standardization, and final data validation, ensuring high-quality data for feature engineering, exploratory data analysis, and visualization.