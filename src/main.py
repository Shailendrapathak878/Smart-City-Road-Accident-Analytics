"""

Smart City Road Accident Analytics
Main Entry Point

"""

from services.loader import DataLoader
from services.cleaner import DataCleaner
from services.feature_engineering import FeatureEngineer
from services.eda import EDAAnalyzer
from services.visualization import Visualization


def main():
    
    # DATA LOADING
    

    loader = DataLoader(
        "../data/raw/accident_dataset.csv"
    )

    dataframe = loader.load_dataset()

    loader.dataset_summary()

   
    # DATA CLEANING
    

    cleaner = DataCleaner(dataframe)

    cleaner.clean()

    cleaner.save_clean_dataset()

    
    # FEATURE ENGINEERING
    

    engineer = FeatureEngineer(
        cleaner.get_dataframe()
    )

    engineer.engineer()

    
    # EDA
    

    eda = EDAAnalyzer(
        engineer.get_dataframe()
    )

    
    # Dataset Overview
    

    eda.dataset_overview()

    eda.column_information()

    eda.datatype_summary()

    eda.missing_summary()

    eda.preview()

    
    # Statistical Summary
    

    eda.numerical_summary()

    eda.categorical_summary()

    eda.unique_values()

   
    # UNIVARIATE ANALYSIS
   
    print("\n")
    print("=" * 70)
    print("UNIVARIATE ANALYSIS")
    print("=" * 70)

    eda.top_states()

    eda.top_districts()

    eda.weather_analysis()

    eda.vehicle_analysis()

    eda.gender_analysis()

    eda.age_group_analysis()

    
    # BIVARIATE ANALYSIS
    

    print("\n")
    print("=" * 70)
    print("BIVARIATE ANALYSIS")
    print("=" * 70)

    eda.weather_vs_severity()

    eda.season_vs_risk()

    eda.vehicle_vs_severity()

    eda.time_vs_severity()

    eda.age_vs_severity()

    eda.risk_vs_severity()

    eda.state_vs_risk()

   
    # VISUALIZATION
   

    visualizer = Visualization(
        engineer.get_dataframe()
    )

    visualizer.generate_all()


if __name__ == "__main__":
    main()