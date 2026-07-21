from services.loader import DataLoader
from services.cleaner import DataCleaner
from services.feature_engineering import FeatureEngineer


def main():

    loader = DataLoader(
        "../data/raw/accident_dataset.csv"
    )

    dataframe = loader.load_dataset()

    loader.dataset_summary()

    # -------------------------
    # Data Cleaning
    # -------------------------

    cleaner = DataCleaner(dataframe)

    cleaner.clean()

    cleaner.save_clean_dataset()

    # -------------------------
    # Feature Engineering
    # -------------------------

    engineer = FeatureEngineer(
        cleaner.get_dataframe()
    )

    engineer.engineer()


if __name__ == "__main__":
    main()