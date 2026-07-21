"""

Smart City Road Accident Analytics
Data Cleaner Module (V3)


Responsible for:
    - Dataset Inspection
    - Data Cleaning
    - Data Validation
    - Data Standardization
    - Dataset Export
"""

import pandas as pd

from config.cleaning_rules import (
    MISSING_VALUE_RULES,
    DUPLICATE_RULES,
    TEXT_STANDARDIZATION_RULES,
    DATA_TYPE_RULES,
    VALIDATION_RULES,
    SAVE_OPTIONS
)


class DataCleaner:
    """
    Professional Data Cleaning Engine.
    """

    
    # Constructor
    

    def __init__(self, dataframe: pd.DataFrame):

        self.dataframe = dataframe.copy()

    
    # Dataset Report
    

    def dataset_report(self):

        print("\n" + "=" * 70)
        print("DATA CLEANING REPORT")
        print("=" * 70)

        print(f"Rows              : {self.dataframe.shape[0]}")
        print(f"Columns           : {self.dataframe.shape[1]}")
        print(
            f"Memory Usage      : "
            f"{round(self.dataframe.memory_usage(deep=True).sum() / 1024 / 1024,2)} MB"
        )

        print("=" * 70)

        self.missing_report()

        self.duplicate_report()

        self.datatype_report()

        self.numeric_summary()

        self.categorical_summary()

    
    # Missing Value Report
   

    def missing_report(self):

        print("\n" + "=" * 70)
        print("MISSING VALUE REPORT")
        print("=" * 70)

        missing = self.dataframe.isnull().sum()

        missing = missing[missing > 0]

        if missing.empty:

            print("No Missing Values Found.")

        else:

            print(missing)

            print()

            print(f"Affected Columns : {len(missing)}")

            print(f"Total Missing    : {missing.sum()}")

        print("=" * 70)

        return missing

   
    # Duplicate Report
   

    def duplicate_report(self):

        duplicates = self.dataframe.duplicated().sum()

        print("\n" + "=" * 70)
        print("DUPLICATE REPORT")
        print("=" * 70)

        print(f"Duplicate Rows : {duplicates}")

        print("=" * 70)

        return duplicates

   
    # Data Type Report
    

    def datatype_report(self):

        print("\n" + "=" * 70)
        print("DATA TYPE REPORT")
        print("=" * 70)

        print(self.dataframe.dtypes)

        print("=" * 70)

        return self.dataframe.dtypes

    
    # Numeric Summary
    

    def numeric_summary(self):

        print("\n" + "=" * 70)
        print("NUMERIC SUMMARY")
        print("=" * 70)

        numeric = self.dataframe.select_dtypes(
            include=["int64", "float64"]
        )

        if numeric.empty:

            print("No Numeric Columns Found.")

        else:

            print(numeric.describe())

        print("=" * 70)

    
    # Categorical Summary
    

    def categorical_summary(self):

        print("\n" + "=" * 70)
        print("CATEGORICAL SUMMARY")
        print("=" * 70)

        categorical = self.dataframe.select_dtypes(
            include=["object", "string"]
        )

        if categorical.empty:

            print("No Categorical Columns Found.")

        else:

            print(categorical.describe())

        print("=" * 70)

           
    # Handle Missing Values (Config Based)
    

    def handle_missing_values(self):

        print("\n" + "=" * 70)
        print("HANDLING MISSING VALUES")
        print("=" * 70)

        for column, rule in MISSING_VALUE_RULES.items():

            if column not in self.dataframe.columns:
                continue

            missing = self.dataframe[column].isnull().sum()

            if missing == 0:
                continue

            method = rule.get("method")

            
            # Median
            

            if method == "median":

                median = self.dataframe[column].median()

                self.dataframe[column] = (
                    self.dataframe[column]
                    .fillna(median)
                )

                print(
                    f"{column:<30}"
                    f"Median Applied ({missing} values)"
                )

           
            # Mode
            

            elif method == "mode":

                mode = self.dataframe[column].mode()[0]

                self.dataframe[column] = (
                    self.dataframe[column]
                    .fillna(mode)
                )

                print(
                    f"{column:<30}"
                    f"Mode Applied ({missing} values)"
                )

           
            # Business Rule
            

            elif method == "business_rule":

                default = rule.get("default")

                self.dataframe[column] = (
                    self.dataframe[column]
                    .fillna(default)
                )

                print(
                    f"{column:<30}"
                    f"Business Rule Applied ({missing} values)"
                )

            
            # Constant Value
            
            elif method == "constant":

                default = rule.get("default")

                self.dataframe[column] = (
                    self.dataframe[column]
                    .fillna(default)
                )

                print(
                    f"{column:<30}"
                    f"Constant Applied ({missing} values)"
                )

        print("=" * 70)

    
    # Apply Business Rules
    

    def apply_business_rules(self):

        print("\n" + "=" * 70)
        print("BUSINESS RULE VALIDATION")
        print("=" * 70)

        # Accident Severity

        if (
            "accident_occurred" in self.dataframe.columns
            and "accident_severity" in self.dataframe.columns
        ):

            mask = self.dataframe["accident_occurred"] == False

            self.dataframe.loc[
                mask,
                "accident_severity"
            ] = "No Accident"

            print("✓ Accident Severity Updated")

        # Property Damage

        if (
            "accident_occurred" in self.dataframe.columns
            and "property_damage" in self.dataframe.columns
        ):

            mask = self.dataframe["accident_occurred"] == False

            self.dataframe.loc[
                mask,
                "property_damage"
            ] = "No"

            print("✓ Property Damage Updated")

        # Response Time

        if (
            "ambulance_required" in self.dataframe.columns
            and "estimated_response_time" in self.dataframe.columns
        ):

            mask = self.dataframe["ambulance_required"] == False

            self.dataframe.loc[
                mask,
                "estimated_response_time"
            ] = 0

            print("✓ Response Time Updated")

        print("=" * 70)

    
    # Remove Duplicate Rows
    

    def remove_duplicates(self):

        if not DUPLICATE_RULES.get("remove_duplicates"):

            return

        print("\n" + "=" * 70)
        print("REMOVING DUPLICATES")
        print("=" * 70)

        before = len(self.dataframe)

        self.dataframe.drop_duplicates(inplace=True)

        after = len(self.dataframe)

        print(
            f"Removed Rows : {before-after}"
        )

        print("=" * 70)

            
    # Fix Data Types
    

    def fix_data_types(self):

        print("\n" + "=" * 70)
        print("FIXING DATA TYPES")
        print("=" * 70)

        for column, dtype in DATA_TYPE_RULES.items():

            if column not in self.dataframe.columns:
                continue

            try:

                if dtype == "datetime":

                    self.dataframe[column] = pd.to_datetime(
                        self.dataframe[column],
                        errors="coerce"
                    )

                elif dtype == "string":

                    self.dataframe[column] = (
                        self.dataframe[column]
                        .astype("string")
                    )

                elif dtype == "int":

                    self.dataframe[column] = (
                        pd.to_numeric(
                            self.dataframe[column],
                            errors="coerce"
                        )
                        .fillna(0)
                        .astype(int)
                    )

                elif dtype == "float":

                    self.dataframe[column] = (
                        pd.to_numeric(
                            self.dataframe[column],
                            errors="coerce"
                        )
                        .astype(float)
                    )

                print(f"✓ {column:<30} -> {dtype}")

            except Exception as e:

                print(f"✗ {column:<30} {e}")

        print("=" * 70)

    
    # Validate Data Ranges
   

    def validate_ranges(self):

        print("\n" + "=" * 70)
        print("VALIDATING DATA")
        print("=" * 70)

        for column, rules in VALIDATION_RULES.items():

            if column not in self.dataframe.columns:
                continue

            minimum = rules["min"]
            maximum = rules["max"]

            invalid = (
                (self.dataframe[column] < minimum)
                |
                (self.dataframe[column] > maximum)
            )

            count = invalid.sum()

            if count > 0:

                median = self.dataframe[column].median()

                self.dataframe.loc[
                    invalid,
                    column
                ] = median

                print(
                    f"{column:<30}"
                    f"{count} invalid values corrected"
                )

        print("=" * 70)

    
    # Standardize Text
    

    def standardize_text(self):

        print("\n" + "=" * 70)
        print("STANDARDIZING TEXT")
        print("=" * 70)

        if TEXT_STANDARDIZATION_RULES["strip_spaces"]:

            object_columns = self.dataframe.select_dtypes(
                include=["object", "string"]
            ).columns

            for column in object_columns:

                self.dataframe[column] = (
                    self.dataframe[column]
                    .astype(str)
                    .str.strip()
                )

        for column in TEXT_STANDARDIZATION_RULES["title_case"]:

            if column in self.dataframe.columns:

                self.dataframe[column] = (
                    self.dataframe[column]
                    .str.title()
                )

        for column in TEXT_STANDARDIZATION_RULES["upper_case"]:

            if column in self.dataframe.columns:

                self.dataframe[column] = (
                    self.dataframe[column]
                    .str.upper()
                )

        print("✓ Text Standardization Completed")

        print("=" * 70)

    
    # Save Clean Dataset
    

    def save_clean_dataset(
        self,
        output_path="../data/cleaned/cleaned_accident_dataset.csv"
    ):

        self.dataframe.to_csv(

            output_path,

            index=SAVE_OPTIONS["index"],

            encoding=SAVE_OPTIONS["encoding"]

        )

        print("\n" + "=" * 70)
        print("CLEAN DATASET SAVED")
        print("=" * 70)

        print(output_path)

        print("=" * 70)

   
    # Return DataFrame
    

    def get_dataframe(self):

        return self.dataframe



            
    # Cleaning Summary
   

    def cleaning_summary(self):

        print("\n" + "=" * 70)
        print("CLEANING SUMMARY")
        print("=" * 70)

        print(f"Rows               : {self.dataframe.shape[0]}")
        print(f"Columns            : {self.dataframe.shape[1]}")

        print(
            f"Remaining Missing  : "
            f"{self.dataframe.isnull().sum().sum()}"
        )

        print(
            f"Duplicate Rows     : "
            f"{self.dataframe.duplicated().sum()}"
        )

        print(
            f"Memory Usage       : "
            f"{round(self.dataframe.memory_usage(deep=True).sum()/1024/1024,2)} MB"
        )

        print("=" * 70)

    
    # Execute Complete Cleaning Pipeline
    

    def clean(self):

        print("\n")
        print("=" * 70)
        print("STARTING DATA CLEANING PIPELINE")
        print("=" * 70)

        self.dataset_report()

        self.handle_missing_values()

        self.apply_business_rules()

        self.remove_duplicates()

        self.fix_data_types()

        self.validate_ranges()

        self.standardize_text()

        self.cleaning_summary()

        print("=" * 70)
        print("DATA CLEANING COMPLETED")
        print("=" * 70)





