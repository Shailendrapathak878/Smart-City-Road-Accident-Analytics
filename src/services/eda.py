"""

Smart City Road Accident Analytics
Exploratory Data Analysis (EDA)


Responsible For:
    - Dataset Overview
    - Dataset Inspection
    - Statistical Summary
"""

import pandas as pd
import numpy as np


class EDAAnalyzer:

    
    # Constructor
    

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe.copy()

    
    # Dataset Overview
    

    def dataset_overview(self):
        print("\n" + "=" * 70)
        print("DATASET OVERVIEW")
        print("=" * 70)

        print(f"Rows              : {self.dataframe.shape[0]}")
        print(f"Columns           : {self.dataframe.shape[1]}")

        memory = round(
            self.dataframe.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )

        print(f"Memory Usage      : {memory} MB")
        print(f"Duplicate Rows    : {self.dataframe.duplicated().sum()}")
        print(f"Missing Values    : {self.dataframe.isnull().sum().sum()}")

        print("=" * 70)

    
    # Column Information
   

    def column_information(self):
        print("\n" + "=" * 70)
        print("COLUMN INFORMATION")
        print("=" * 70)

        for index, column in enumerate(self.dataframe.columns, start=1):
            print(f"{index:02d}. {column}")

        print("=" * 70)

    
    # Data Types
   

    def datatype_summary(self):
        print("\n" + "=" * 70)
        print("DATA TYPE SUMMARY")
        print("=" * 70)

        print(self.dataframe.dtypes)

        print("=" * 70)

    
    # Missing Values
    

    def missing_summary(self):
        print("\n" + "=" * 70)
        print("MISSING VALUE SUMMARY")
        print("=" * 70)

        missing = self.dataframe.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) == 0:
            print("✓ No Missing Values Found")
        else:
            print(missing)

        print("=" * 70)

    
    # Dataset Preview
    

    def preview(self):
        print("\n" + "=" * 70)
        print("DATASET PREVIEW")
        print("=" * 70)

        print(self.dataframe.head())

        print("=" * 70)

    
    

    def numerical_summary(self):
        print("\n" + "=" * 70)
        print("NUMERICAL SUMMARY")
        print("=" * 70)

        summary = self.dataframe.describe()
        print(summary)

        print("=" * 70)

    
    # Categorical Summary
   

    def categorical_summary(self):
        print("\n" + "=" * 70)
        print("CATEGORICAL SUMMARY")
        print("=" * 70)

        summary = self.dataframe.describe(include=["object", "string"])
        print(summary)

        print("=" * 70)

    
    # Unique Values Summary
    

    def unique_values(self):
        print("\n" + "=" * 70)
        print("UNIQUE VALUES SUMMARY")
        print("=" * 70)

        for column in self.dataframe.columns:
            unique_count = self.dataframe[column].nunique()
            print(f"{column:<35} : {unique_count}")

        print("=" * 70)

    
    # Top Records
    

    def top_records(self, rows=10):
        print("\n" + "=" * 70)
        print(f"TOP {rows} RECORDS")
        print("=" * 70)

        print(self.dataframe.head(rows))

        print("=" * 70)

    
    # Bottom Records
    

    def bottom_records(self, rows=10):
        print("\n" + "=" * 70)
        print(f"BOTTOM {rows} RECORDS")
        print("=" * 70)

        print(self.dataframe.tail(rows))

        print("=" * 70)

    
    # Distribution Helper
    

    def distribution(self, column):
        print("\n" + "=" * 70)
        print(f"{column.upper()} DISTRIBUTION")
        print("=" * 70)

        if column not in self.dataframe.columns:
            print("Column Not Found")
            return

        result = self.dataframe[column].value_counts()
        percentage = (self.dataframe[column].value_counts(normalize=True) * 100).round(2)

        summary = pd.DataFrame({
            "Count": result,
            "Percentage": percentage
        })

        print(summary)
        print("=" * 70)

   
    
    def top_states(self):
        self.distribution("state_name")

    
    # Top Districts
   

    def top_districts(self):
        self.distribution("district_name")

    
    # Weather Analysis
    

    def weather_analysis(self):
        self.distribution("weather_name")

    
    # Vehicle Analysis 

    def vehicle_analysis(self):
        self.distribution("vehicle_type")

    
    # Driver Gender
    

    def gender_analysis(self):
        self.distribution("driver_gender")


   
    # Driver Age Group Analysis
   

    def age_group_analysis(self):

        self.distribution("driver_age_group")


            
    # Weather vs Accident Severity
    

    def weather_vs_severity(self):

        print("\n" + "=" * 70)
        print("WEATHER VS ACCIDENT SEVERITY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["weather_name"],

            self.dataframe["accident_severity"]

        )

        print(table)

        print("=" * 70)

    
    # Season vs Risk Band
    

    def season_vs_risk(self):

        print("\n" + "=" * 70)
        print("SEASON VS RISK BAND")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["season"],

            self.dataframe["risk_band"]

        )

        print(table)

        print("=" * 70)

   
    # Vehicle Type vs Severity
    
    def vehicle_vs_severity(self):

        print("\n" + "=" * 70)
        print("VEHICLE TYPE VS ACCIDENT SEVERITY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["vehicle_type"],

            self.dataframe["accident_severity"]

        )

        print(table)

        print("=" * 70)

   
    # Time Of Day vs Severity
    
    def time_vs_severity(self):

        print("\n" + "=" * 70)
        print("TIME OF DAY VS ACCIDENT SEVERITY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["time_of_day"],

            self.dataframe["accident_severity"]

        )

        print(table)

        print("=" * 70)

    
    # Driver Age Group vs Severity
    

    def age_vs_severity(self):

        print("\n" + "=" * 70)
        print("AGE GROUP VS ACCIDENT SEVERITY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["driver_age_group"],

            self.dataframe["accident_severity"]

        )

        print(table)

        print("=" * 70)

    
    # Risk Band vs Severity
    

    def risk_vs_severity(self):

        print("\n" + "=" * 70)
        print("RISK BAND VS ACCIDENT SEVERITY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["risk_band"],

            self.dataframe["accident_severity"]

        )

        print(table)

        print("=" * 70)

   
    # State vs Risk Category
    

    def state_vs_risk(self):

        print("\n" + "=" * 70)
        print("STATE VS RISK CATEGORY")
        print("=" * 70)

        table = pd.crosstab(

            self.dataframe["state_name"],

            self.dataframe["risk_category"]

        )

        print(table)

        print("=" * 70)