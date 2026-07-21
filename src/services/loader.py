"""
Data Loader Module

Loads the IRAAD accident dataset and provides
basic dataset inspection utilities.
"""

import os
import pandas as pd


class DataLoader:
    """
    DataLoader handles loading and inspecting
    the road accident dataset.
    """

    def __init__(self, dataset_path: str):
        """
        Initialize DataLoader.

        Parameters
        ----------
        dataset_path : str
            Path to dataset CSV file.
        """
        self.dataset_path = dataset_path
        self.dataframe = None

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_dataset(self):
        """
        Load CSV dataset.

        Returns
        -------
        pandas.DataFrame
        """

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset not found:\n{self.dataset_path}"
            )

        if not self.dataset_path.endswith(".csv"):
            raise ValueError(
                "Only CSV files are supported."
            )

        try:

            self.dataframe = pd.read_csv(self.dataset_path)

            if self.dataframe.empty:
                raise ValueError(
                    "Dataset is empty."
                )

            print("\nDataset Loaded Successfully.\n")

            return self.dataframe

        except Exception as e:
            raise Exception(
                f"Error loading dataset:\n{e}"
            )

    # =====================================================
    # Preview Dataset
    # =====================================================

    def preview(self, rows=5):
        """
        Display first rows.
        """

        return self.dataframe.head(rows)

    # =====================================================
    # Dataset Shape
    # =====================================================

    def dataset_shape(self):
        """
        Returns dataset shape.
        """

        return self.dataframe.shape

    # =====================================================
    # Column Names
    # =====================================================

    def column_names(self):
        """
        Returns all column names.
        """

        return list(self.dataframe.columns)

    # =====================================================
    # Data Types
    # =====================================================

    def data_types(self):
        """
        Returns datatype of every column.
        """

        return self.dataframe.dtypes

    # =====================================================
    # Missing Values
    # =====================================================

    def missing_values(self):
        """
        Returns missing values.
        """

        return self.dataframe.isnull().sum()

    # =====================================================
    # Duplicate Rows
    # =====================================================

    def duplicate_rows(self):
        """
        Returns duplicate row count.
        """

        return self.dataframe.duplicated().sum()

    # =====================================================
    # Memory Usage
    # =====================================================

    def memory_usage(self):
        """
        Returns memory usage in MB.
        """

        memory = (
            self.dataframe.memory_usage(deep=True).sum()
            / (1024 * 1024)
        )

        return round(memory, 2)

    # =====================================================
    # Dataset Summary
    # =====================================================

    def dataset_summary(self):
        """
        Display complete dataset summary.
        """

        rows, columns = self.dataset_shape()

        print("=" * 60)
        print("SMART CITY ROAD ACCIDENT ANALYTICS")
        print("=" * 60)

        print(f"Dataset Path      : {self.dataset_path}")
        print(f"Rows              : {rows}")
        print(f"Columns           : {columns}")
        print(f"Memory Usage      : {self.memory_usage()} MB")
        print(f"Duplicate Rows    : {self.duplicate_rows()}")
        print(
            f"Missing Values    : {self.missing_values().sum()}"
        )

        print("=" * 60)

    # =====================================================
    # Get DataFrame
    # =====================================================

    def get_dataframe(self):
        """
        Returns loaded DataFrame.
        """

        return self.dataframe