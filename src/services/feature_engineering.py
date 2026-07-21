"""

Smart City Road Accident Analytics
Feature Engineering Module


Responsible For:
    - Feature Creation
    - Data Enrichment
    - Preparing Dataset for EDA
    - Preparing Dataset for Machine Learning
"""

import numpy as np
import pandas as pd


class FeatureEngineer:

    
    # Constructor
    

    def __init__(self, dataframe: pd.DataFrame):

        self.dataframe = dataframe.copy()

   
    # Time Of Day
   

    def create_time_of_day(self):

        print("\n" + "=" * 70)
        print("CREATING TIME OF DAY")
        print("=" * 70)

        conditions = [

            self.dataframe["hour"].between(5, 11),

            self.dataframe["hour"].between(12, 16),

            self.dataframe["hour"].between(17, 20),

            (
                self.dataframe["hour"] >= 21
            ) | (
                self.dataframe["hour"] <= 4
            )

        ]

        choices = [

            "Morning",

            "Afternoon",

            "Evening",

            "Night"

        ]

        self.dataframe["time_of_day"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ time_of_day created")

   
    # Driver Age Group
    

    def create_age_group(self):

        print("\n" + "=" * 70)
        print("CREATING DRIVER AGE GROUP")
        print("=" * 70)

        conditions = [

            self.dataframe["driver_age"] <= 25,

            self.dataframe["driver_age"].between(26, 40),

            self.dataframe["driver_age"].between(41, 60),

            self.dataframe["driver_age"] > 60

        ]

        choices = [

            "Young",

            "Adult",

            "Middle Age",

            "Senior"

        ]

        self.dataframe["driver_age_group"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ driver_age_group created")

    
    # Season
    

    def create_season(self):

        print("\n" + "=" * 70)
        print("CREATING SEASON")
        print("=" * 70)

        conditions = [

            self.dataframe["month"].isin([12, 1, 2]),

            self.dataframe["month"].isin([3, 4, 5]),

            self.dataframe["month"].isin([6, 7, 8, 9]),

            self.dataframe["month"].isin([10, 11])

        ]

        choices = [

            "Winter",

            "Summer",

            "Monsoon",

            "Post Monsoon"

        ]

        self.dataframe["season"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ season created")

            
    # Speed Category
    

    def create_speed_category(self):

        print("\n" + "=" * 70)
        print("CREATING SPEED CATEGORY")
        print("=" * 70)

        conditions = [

            self.dataframe["average_speed"] < 30,

            self.dataframe["average_speed"].between(30, 60),

            self.dataframe["average_speed"] > 60

        ]

        choices = [

            "Low",

            "Medium",

            "High"

        ]

        self.dataframe["speed_category"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ speed_category created")

   
    # Risk Band
    

    def create_risk_band(self):

        print("\n" + "=" * 70)
        print("CREATING RISK BAND")
        print("=" * 70)

        conditions = [

            self.dataframe["risk_score"] < 20,

            self.dataframe["risk_score"].between(20, 40),

            self.dataframe["risk_score"].between(41, 60),

            self.dataframe["risk_score"].between(61, 80),

            self.dataframe["risk_score"] > 80

        ]

        choices = [

            "Very Low",

            "Low",

            "Moderate",

            "High",

            "Very High"

        ]

        self.dataframe["risk_band"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ risk_band created")

    
    # Month Name
    

    def create_month_name(self):

        print("\n" + "=" * 70)
        print("CREATING MONTH NAME")
        print("=" * 70)

        month_map = {

            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"

        }

        self.dataframe["month_name"] = (

            self.dataframe["month"]

            .map(month_map)

        )

        print("✓ month_name created")

    
    # Quarter
   

    def create_quarter(self):

        print("\n" + "=" * 70)
        print("CREATING QUARTER")
        print("=" * 70)

        conditions = [

            self.dataframe["month"].between(1, 3),

            self.dataframe["month"].between(4, 6),

            self.dataframe["month"].between(7, 9),

            self.dataframe["month"].between(10, 12)

        ]

        choices = [

            "Q1",

            "Q2",

            "Q3",

            "Q4"

        ]

        self.dataframe["quarter"] = np.select(

            conditions,

            choices,

            default="Unknown"

        )

        print("✓ quarter created")

   
    # Peak Hour
   

    def create_peak_hour(self):

        print("\n" + "=" * 70)
        print("CREATING PEAK HOUR")
        print("=" * 70)

        self.dataframe["is_peak_hour"] = (

            self.dataframe["hour"].between(8, 10)

            |

            self.dataframe["hour"].between(17, 20)

        )

        print("✓ is_peak_hour created")


            
    # Feature Summary
   

    def feature_summary(self):

        print("\n" + "=" * 70)
        print("FEATURE ENGINEERING SUMMARY")
        print("=" * 70)

        print(f"Rows    : {self.dataframe.shape[0]}")
        print(f"Columns : {self.dataframe.shape[1]}")

        print("\nNew Features Added")
        print("-" * 40)

        features = [

            "time_of_day",
            "driver_age_group",
            "season",
            "speed_category",
            "risk_band",
            "month_name",
            "quarter",
            "is_peak_hour"

        ]

        for feature in features:

            print(f"✓ {feature}")

        print("=" * 70)

    
    # Save Featured Dataset
    

    def save_featured_dataset(
        self,
        output_path="../data/featured/featured_accident_dataset.csv"
    ):

        import os

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        self.dataframe.to_csv(

            output_path,

            index=False

        )

        print("\n" + "=" * 70)
        print("FEATURED DATASET SAVED")
        print("=" * 70)
        print(output_path)
        print("=" * 70)

   
    # Execute Feature Engineering Pipeline
    

    def engineer(self):

        print("\n")
        print("=" * 70)
        print("STARTING FEATURE ENGINEERING")
        print("=" * 70)

        self.create_time_of_day()

        self.create_age_group()

        self.create_season()

        self.create_speed_category()

        self.create_risk_band()

        self.create_month_name()

        self.create_quarter()

        self.create_peak_hour()

        self.feature_summary()

        self.save_featured_dataset()

        print("=" * 70)
        print("FEATURE ENGINEERING COMPLETED")
        print("=" * 70)

   
    # Return DataFrame
   
    def get_dataframe(self):

        return self.dataframe



