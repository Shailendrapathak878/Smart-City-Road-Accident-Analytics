"""
============================================================
Smart City Road Accident Analytics
Feature Engineering Module
============================================================

Responsible for:
    - Creating New Features
    - Improving Dataset Quality
    - Preparing Data for EDA & ML
"""

import numpy as np
import pandas as pd


class FeatureEngineer:

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(self, dataframe: pd.DataFrame):

        self.dataframe = dataframe.copy()

    # =====================================================
    # Time Of Day
    # =====================================================

    def create_time_of_day(self):

        print("\n" + "=" * 70)
        print("CREATING TIME OF DAY")
        print("=" * 70)

        conditions = [

            self.dataframe["hour"].between(5, 11),

            self.dataframe["hour"].between(12, 16),

            self.dataframe["hour"].between(17, 20),

            (self.dataframe["hour"] >= 21)
            | (self.dataframe["hour"] <= 4)

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

    # =====================================================
    # Driver Age Group
    # =====================================================

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

    # =====================================================
    # Season
    # =====================================================

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

    # =====================================================
    # Feature Summary
    # =====================================================

    def feature_summary(self):

        print("\n" + "=" * 70)
        print("FEATURE ENGINEERING SUMMARY")
        print("=" * 70)

        print(f"Rows    : {self.dataframe.shape[0]}")

        print(f"Columns : {self.dataframe.shape[1]}")

        print("\nNew Features Added")

        print("-------------------------")

        print("✓ time_of_day")

        print("✓ driver_age_group")

        print("✓ season")

        print("=" * 70)

    # =====================================================
    # Execute Pipeline
    # =====================================================

    def engineer(self):

        print("\n")
        print("=" * 70)
        print("STARTING FEATURE ENGINEERING")
        print("=" * 70)

        self.create_time_of_day()

        self.create_age_group()

        self.create_season()

        self.feature_summary()

        print("=" * 70)
        print("FEATURE ENGINEERING COMPLETED")
        print("=" * 70)

    # =====================================================
    # Return DataFrame
    # =====================================================

    def get_dataframe(self):

        return self.dataframe