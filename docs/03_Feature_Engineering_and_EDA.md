# Feature Engineering and Exploratory Data Analysis (EDA)

---

# Introduction

After cleaning the dataset, the next step is to improve the quality of the data by creating meaningful features and performing exploratory data analysis (EDA).

Feature Engineering helps generate new information from existing data, while Exploratory Data Analysis helps understand patterns, relationships, trends, and distributions within the dataset.

---

# Feature Engineering

## What is Feature Engineering?

Feature Engineering is the process of creating new variables (features) from existing columns to improve data analysis and make the dataset more informative.

The project automatically creates multiple useful features from the cleaned dataset.

---

# Engineered Features

## 1. Time of Day

Created using the **Hour** column.

| Hour | Time of Day |
|------|-------------|
| 05 – 11 | Morning |
| 12 – 16 | Afternoon |
| 17 – 20 | Evening |
| 21 – 04 | Night |

Purpose:

- Analyze accidents throughout the day.
- Identify high-risk time periods.

---

## 2. Driver Age Group

Created from the **Driver Age** column.

| Age | Category |
|------|-----------|
| ≤25 | Young |
| 26 – 40 | Adult |
| 41 – 60 | Middle Age |
| >60 | Senior |

Purpose:

- Compare accident frequency across age groups.
- Study driver behavior by age.

---

## 3. Season

Created using the **Month** column.

| Months | Season |
|---------|---------|
| Dec – Feb | Winter |
| Mar – May | Summer |
| Jun – Sep | Monsoon |
| Oct – Nov | Post Monsoon |

Purpose:

- Analyze seasonal accident trends.
- Identify weather-related risks.

---

## 4. Speed Category

Created using the **Average Speed** column.

| Speed | Category |
|--------|----------|
| <30 km/h | Low |
| 30–60 km/h | Medium |
| >60 km/h | High |

Purpose:

- Compare accident risk at different speed ranges.
- Analyze speed-related accident patterns.

---

## 5. Risk Band

Created using the **Risk Score** column.

| Risk Score | Category |
|-------------|----------|
| <20 | Very Low |
| 20–40 | Low |
| 41–60 | Moderate |
| 61–80 | High |
| >80 | Very High |

Purpose:

- Simplify interpretation of risk scores.
- Improve visualization and reporting.

---

## 6. Month Name

Converts numeric month values into readable month names.

Example:

| Month | Name |
|--------|------|
| 1 | January |
| 2 | February |
| ... | ... |
| 12 | December |

Purpose:

- Improve chart readability.
- Enhance reporting.

---

## 7. Quarter

Created using the Month column.

| Months | Quarter |
|---------|----------|
| Jan – Mar | Q1 |
| Apr – Jun | Q2 |
| Jul – Sep | Q3 |
| Oct – Dec | Q4 |

Purpose:

- Quarterly accident analysis.
- Business reporting.

---

## 8. Peak Hour Indicator

Created using the Hour column.

Peak Hours:

- 08:00 – 10:00
- 17:00 – 20:00

Values:

- True
- False

Purpose:

- Identify rush-hour accidents.
- Compare peak vs non-peak accident rates.

---

# Feature Engineering Workflow

```text
Clean Dataset
      │
      ▼
Create Time of Day
      │
      ▼
Create Driver Age Group
      │
      ▼
Create Season
      │
      ▼
Create Speed Category
      │
      ▼
Create Risk Band
      │
      ▼
Create Month Name
      │
      ▼
Create Quarter
      │
      ▼
Create Peak Hour
      │
      ▼
Featured Dataset
```

---

# Feature Engineering Output

The processed dataset is automatically saved.

```text
data/

└── featured/

    └── featured_accident_dataset.csv
```

---

# Exploratory Data Analysis (EDA)

## What is EDA?

Exploratory Data Analysis (EDA) is the process of analyzing data using statistical summaries and visual techniques to discover hidden patterns, detect anomalies, and understand relationships between variables.

---

# Statistical Analysis Performed

The project performs:

- Dataset Summary
- Missing Value Analysis
- Duplicate Analysis
- Data Type Analysis
- Numerical Statistics
- Categorical Statistics
- Correlation Analysis
- Frequency Distribution

---

# Numerical Analysis

For numerical columns, the project calculates:

- Count
- Mean
- Median
- Standard Deviation
- Minimum
- Maximum
- Quartiles
- Percentiles

These statistics help understand the overall distribution of numeric variables.

---

# Categorical Analysis

Categorical columns are analyzed using:

- Frequency Count
- Unique Values
- Most Frequent Category
- Category Distribution

---

# Correlation Analysis

Correlation is calculated between numerical variables to identify relationships.

Purpose:

- Detect strong correlations.
- Support feature selection.
- Understand variable dependencies.

---

# Distribution Analysis

The project studies the distribution of:

- Driver Age
- Average Speed
- Risk Score
- Accident Severity
- Vehicle Type
- Weather Condition
- State
- Season

This helps identify common trends and unusual patterns.

---

# Key Benefits

Feature Engineering and EDA provide:

- Better data understanding
- Improved analytical quality
- Easier visualization
- More meaningful business insights
- Better dataset interpretation
- Enhanced reporting

---

# Output

The EDA process produces:

```text
Console Reports

✔ Dataset Summary

✔ Statistical Summary

✔ Correlation Information

✔ Frequency Analysis

Visualization

✔ Bar Charts

✔ Pie Charts

✔ Histograms

✔ Scatter Plots

✔ Heatmaps

✔ Box Plots

✔ Violin Plots
```

---

# Summary

Feature Engineering enhances the dataset by generating meaningful new variables, while Exploratory Data Analysis provides a comprehensive understanding of the data through statistical summaries and pattern discovery.

Together, these processes prepare the dataset for professional visualization and enable accurate interpretation of road accident trends and risk factors.