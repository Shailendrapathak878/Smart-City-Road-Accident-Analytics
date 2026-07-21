from services.loader import DataLoader
from services.cleaner import DataCleaner


def main():

    loader = DataLoader(
        "../data/raw/accident_dataset.csv"
    )

    dataframe = loader.load_dataset()

    loader.dataset_summary()

    cleaner = DataCleaner(dataframe)

    cleaner.clean()

    cleaner.save_clean_dataset()


if __name__ == "__main__":
    main()