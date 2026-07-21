"""

Visualization Module

Creates Professional Charts
Saves Charts Automatically
"""

import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, List, Dict, Tuple


class Visualization:
    """Enterprise-grade visualization module for Smart City Road Accident Analytics."""

    # Configuration constants
    DPI = 300
    TITLE_SIZE = 16
    LABEL_SIZE = 12
    TICK_SIZE = 11
    FONT_WEIGHT = 'bold'
    DEFAULT_PALETTE = "deep"
    TOP_N = 10
    TOP_N_PIE = 8
    ROTATION = 45
    GRID_ALPHA = 0.3

    OUTPUT_BASE = "../outputs"
    CHARTS_DIR = f"{OUTPUT_BASE}/charts"
    REPORT_DIR = f"{OUTPUT_BASE}/reports"

    FIGSIZE_BAR = (14, 8)
    FIGSIZE_HIST = (11, 7)
    FIGSIZE_PIE = (10, 10)
    FIGSIZE_HEATMAP = (13, 10)
    FIGSIZE_SCATTER = (11, 7)
    FIGSIZE_BOX = (11, 7)
    FIGSIZE_VIOLIN = (10, 7)

   
   
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe.copy()
        self.chart_count = 0
        self._chart_stats: Dict[str, int] = {
            "bar": 0, "pie": 0, "histogram": 0, "scatter": 0,
            "heatmap": 0, "boxplot": 0, "violin": 0
        }
        
        sns.set_theme(
            style="whitegrid",
            palette=self.DEFAULT_PALETTE,
            font_scale=1.2
        )
        
        self._setup_directories()

    def _setup_directories(self) -> None:
        """Create all required output directories."""
        dirs = [
            f"{self.CHARTS_DIR}/bar",
            f"{self.CHARTS_DIR}/pie",
            f"{self.CHARTS_DIR}/histogram",
            f"{self.CHARTS_DIR}/scatter",
            f"{self.CHARTS_DIR}/heatmap",
            f"{self.CHARTS_DIR}/boxplot",
            f"{self.CHARTS_DIR}/violin",
            self.REPORT_DIR,
            f"{self.OUTPUT_BASE}/dashboard"
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

   
    # Helper Methods
   

    def _create_figure(self, figsize: Tuple[int, int]) -> plt.Figure:
        """Reusable figure creation helper."""
        return plt.figure(figsize=figsize)

    def _set_title(self, ax: plt.Axes, title: str) -> None:
        """Set professional chart title."""
        ax.set_title(title, fontsize=self.TITLE_SIZE, fontweight=self.FONT_WEIGHT, pad=20)

    def _add_value_labels(self, ax: plt.Axes, padding: int = 3) -> None:
        """Add value labels to bars with consistent styling."""
        for container in ax.containers:
            ax.bar_label(container, padding=padding, fontsize=10, fontweight='bold')

    def _save_chart(self, filename: str, folder: str = "bar") -> None:
        """Enhanced save with comprehensive error handling."""
        self.chart_count += 1
        self._chart_stats[folder] = self._chart_stats.get(folder, 0) + 1

        path = f"{self.CHARTS_DIR}/{folder}/{filename}"

        try:
            plt.tight_layout()
            plt.savefig(path, dpi=self.DPI, bbox_inches="tight")
            print(f"[{self.chart_count}] Saved -> {path}")
        except Exception as e:
            print(f"[ERROR] Failed to save {filename}: {str(e)}")
        finally:
            plt.close()

    
    # State Distribution
   

    def state_distribution_chart(self):
        """Generate top states bar chart using Seaborn."""
        print("\nCreating State Distribution Chart...")
        
        fig = self._create_figure(self.FIGSIZE_BAR)
        ax = fig.add_subplot(111)
        
        counts = self.dataframe["state_name"].value_counts().head(self.TOP_N)
        sns.barplot(x=counts.index, y=counts.values, ax=ax, palette=self.DEFAULT_PALETTE)
        
        self._set_title(ax, "Top 10 States by Road Accidents")
        ax.set_xlabel("State", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        plt.xticks(rotation=self.ROTATION, ha='right')
        
        self._add_value_labels(ax)
        self._save_chart("state_distribution.png", folder="bar")

   
    # Weather Distribution

    def weather_distribution_chart(self):
        """Generate weather distribution chart."""
        print("\nCreating Weather Distribution Chart...")
        
        fig = self._create_figure(self.FIGSIZE_BAR)
        ax = fig.add_subplot(111)
        
        counts = self.dataframe["weather_name"].value_counts().head(self.TOP_N)
        sns.barplot(x=counts.index, y=counts.values, ax=ax, palette=self.DEFAULT_PALETTE)
        
        self._set_title(ax, "Accidents by Weather Conditions (Top 10)")
        ax.set_xlabel("Weather Condition", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        plt.xticks(rotation=self.ROTATION, ha='right')
        
        self._add_value_labels(ax)
        self._save_chart("weather_distribution.png", folder="bar")

    
    # Vehicle Distribution
   

    def vehicle_distribution_chart(self):
        """Generate vehicle type distribution."""
        print("\nCreating Vehicle Distribution Chart...")
        
        fig = self._create_figure(self.FIGSIZE_BAR)
        ax = fig.add_subplot(111)
        
        counts = self.dataframe["vehicle_type"].value_counts().head(self.TOP_N)
        sns.barplot(x=counts.index, y=counts.values, ax=ax, palette=self.DEFAULT_PALETTE)
        
        self._set_title(ax, "Distribution of Vehicle Types in Accidents (Top 10)")
        ax.set_xlabel("Vehicle Type", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        plt.xticks(rotation=self.ROTATION, ha='right')
        
        self._add_value_labels(ax)
        self._save_chart("vehicle_distribution.png", folder="bar")

    
    # Driver Gender Distribution
    

    def gender_distribution_chart(self):
        """Generate driver gender distribution."""
        print("\nCreating Driver Gender Chart...")
        
        fig = self._create_figure((8, 7))
        ax = fig.add_subplot(111)
        
        sns.countplot(data=self.dataframe, x="driver_gender", hue="driver_gender", 
                     legend=False, palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Driver Gender Distribution")
        ax.set_xlabel("Gender", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Drivers", fontsize=self.LABEL_SIZE)
        
        self._add_value_labels(ax)
        self._save_chart("gender_distribution.png", folder="bar")

    
    # Driver Age Group Distribution
   

    def age_group_distribution_chart(self):
        """Generate age group distribution."""
        print("\nCreating Driver Age Group Chart...")
        
        fig = self._create_figure((10, 7))
        ax = fig.add_subplot(111)
        
        order = ["Young", "Adult", "Middle Age", "Senior"]
        sns.countplot(data=self.dataframe, x="driver_age_group", order=order,
                     hue="driver_age_group", legend=False, palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Driver Age Group Distribution")
        ax.set_xlabel("Age Group", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Drivers", fontsize=self.LABEL_SIZE)
        
        self._add_value_labels(ax)
        self._save_chart("driver_age_group.png", folder="bar")

    
    # Accident Severity
   

    def severity_distribution_chart(self):
        """Generate severity distribution."""
        print("\nCreating Severity Chart...")
        
        fig = self._create_figure((10, 7))
        ax = fig.add_subplot(111)
        
        sns.countplot(data=self.dataframe, x="accident_severity", hue="accident_severity",
                     legend=False, palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Accident Severity Distribution")
        ax.set_xlabel("Severity Level", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        
        self._add_value_labels(ax)
        self._save_chart("severity_distribution.png", folder="bar")

   
    # Risk Band Distribution
    

    def risk_band_chart(self):
        """Generate risk band distribution."""
        print("\nCreating Risk Band Chart...")
        
        fig = self._create_figure((11, 7))
        ax = fig.add_subplot(111)
        
        order = ["Very Low", "Low", "Moderate", "High", "Very High"]
        sns.countplot(data=self.dataframe, x="risk_band", order=order,
                     hue="risk_band", legend=False, palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Risk Band Distribution")
        ax.set_xlabel("Risk Band", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        
        self._add_value_labels(ax)
        self._save_chart("risk_band_distribution.png", folder="bar")

   
    # Vehicle Type Pie Chart
    

    def vehicle_pie_chart(self):
        """Generate enhanced pie chart with smart grouping."""
        print("\nCreating Vehicle Pie Chart...")
        
        fig = self._create_figure(self.FIGSIZE_PIE)
        
        counts = self.dataframe["vehicle_type"].value_counts()
        if len(counts) > self.TOP_N_PIE:
            top_counts = counts.head(self.TOP_N_PIE).copy()
            others_sum = counts[self.TOP_N_PIE:].sum()
            top_counts["Others"] = others_sum
        else:
            top_counts = counts
        
        # Explode only the largest slice
        explode = [0.1 if i == 0 else 0 for i in range(len(top_counts))]
        
        plt.pie(top_counts.values, labels=top_counts.index, autopct='%1.1f%%',
                startangle=90, shadow=True, colors=sns.color_palette(self.DEFAULT_PALETTE),
                explode=explode)
        
        plt.title("Vehicle Type Distribution in Road Accidents", 
                 fontsize=self.TITLE_SIZE, fontweight=self.FONT_WEIGHT, pad=20)
        plt.axis('equal')
        
        self._save_chart("vehicle_pie_chart.png", folder="pie")

   
    # Driver Age Histogram
    

    def driver_age_histogram(self):
        """Generate histogram with optimal bins."""
        print("\nCreating Driver Age Histogram...")
        
        fig = self._create_figure(self.FIGSIZE_HIST)
        ax = fig.add_subplot(111)
        
        sns.histplot(data=self.dataframe, x="driver_age", bins='auto', kde=True,
                    color=sns.color_palette(self.DEFAULT_PALETTE)[3], ax=ax)
        
        self._set_title(ax, "Distribution of Driver Ages")
        ax.set_xlabel("Driver Age (years)", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Frequency", fontsize=self.LABEL_SIZE)
        
        self._save_chart("driver_age_histogram.png", folder="histogram")

    
    # Risk Score Histogram
    

    def risk_score_histogram(self):
        """Generate risk score histogram."""
        print("\nCreating Risk Score Histogram...")
        
        fig = self._create_figure(self.FIGSIZE_HIST)
        ax = fig.add_subplot(111)
        
        sns.histplot(data=self.dataframe, x="risk_score", bins='auto', kde=True,
                    color=sns.color_palette(self.DEFAULT_PALETTE)[4], ax=ax)
        
        self._set_title(ax, "Distribution of Risk Scores")
        ax.set_xlabel("Risk Score", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Frequency", fontsize=self.LABEL_SIZE)
        
        self._save_chart("risk_score_histogram.png", folder="histogram")

   
    # Average Speed Box Plot
    

    def speed_boxplot(self):
        """Generate enhanced box plot."""
        print("\nCreating Speed Box Plot...")
        
        fig = self._create_figure(self.FIGSIZE_BOX)
        ax = fig.add_subplot(111)
        
        sns.boxplot(data=self.dataframe, x="average_speed",
                   color=sns.color_palette(self.DEFAULT_PALETTE)[5], ax=ax,
                   flierprops={"marker": "o", "markerfacecolor": "red"})
        
        self._set_title(ax, "Distribution of Average Vehicle Speeds")
        ax.set_xlabel("Average Speed (km/h)", fontsize=self.LABEL_SIZE)
        
        self._save_chart("speed_boxplot.png", folder="boxplot")

    
    # Season Count Plot
    

    def season_countplot(self):
        """Generate season count plot."""
        print("\nCreating Season Count Plot...")
        
        fig = self._create_figure((10, 7))
        ax = fig.add_subplot(111)
        
        sns.countplot(data=self.dataframe, x="season", hue="season",
                     legend=False, palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Accidents by Season")
        ax.set_xlabel("Season", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        
        self._add_value_labels(ax)
        self._save_chart("season_countplot.png", folder="bar")

   
    # Correlation Heatmap
    

    def correlation_heatmap(self):
        """Generate dynamic correlation heatmap."""
        print("\nCreating Correlation Heatmap...")
        
        numeric_df = self.dataframe.select_dtypes(include="number")
        n_cols = len(numeric_df.columns)
        
        figsize = (max(12, n_cols * 0.8), max(10, n_cols * 0.7))
        fig = self._create_figure(figsize)
        ax = fig.add_subplot(111)
        
        corr_matrix = numeric_df.corr()
        annot = n_cols <= 12
        
        sns.heatmap(corr_matrix, annot=annot, fmt=".2f", cmap="coolwarm",
                   center=0, square=True, linewidths=0.5, ax=ax,
                   cbar_kws={"shrink": .8})
        
        self._set_title(ax, "Correlation Heatmap of Numerical Features")
        plt.xticks(rotation=45, ha='right')
        
        self._save_chart("correlation_heatmap.png", folder="heatmap")

    
    # Speed vs Risk Score
    

    def speed_vs_risk_scatter(self):
        """Generate enhanced scatter plot with regression."""
        print("\nCreating Speed vs Risk Scatter Plot...")
        
        fig = self._create_figure(self.FIGSIZE_SCATTER)
        ax = fig.add_subplot(111)
        
        sns.regplot(data=self.dataframe, x="average_speed", y="risk_score",
                   scatter_kws={'alpha': 0.7, 's': 60, 'edgecolor': 'w'},
                   line_kws={'color': 'red'}, ax=ax)
        
        self._set_title(ax, "Average Speed vs Risk Score Relationship")
        ax.set_xlabel("Average Speed (km/h)", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Risk Score", fontsize=self.LABEL_SIZE)
        
        self._save_chart("speed_vs_risk_scatter.png", folder="scatter")

    
    # Risk Score by Season
    

    def season_risk_boxplot(self):
        """Generate season risk boxplot."""
        print("\nCreating Season Risk Boxplot...")
        
        fig = self._create_figure(self.FIGSIZE_BOX)
        ax = fig.add_subplot(111)
        
        sns.boxplot(data=self.dataframe, x="season", y="risk_score",
                   palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Risk Score Distribution by Season")
        ax.set_xlabel("Season", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Risk Score", fontsize=self.LABEL_SIZE)
        
        self._save_chart("season_risk_boxplot.png", folder="boxplot")

   
    # Driver Age Violin Plot
    

    def driver_age_violin(self):
        """Generate violin plot."""
        print("\nCreating Driver Age Violin Plot...")
        
        fig = self._create_figure(self.FIGSIZE_VIOLIN)
        ax = fig.add_subplot(111)
        
        sns.violinplot(data=self.dataframe, x="driver_gender", y="driver_age",
                      palette=self.DEFAULT_PALETTE, inner="quartile", ax=ax)
        
        self._set_title(ax, "Driver Age Distribution by Gender")
        ax.set_xlabel("Driver Gender", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Driver Age (years)", fontsize=self.LABEL_SIZE)
        
        self._save_chart("driver_age_violin.png", folder="violin")

    
    # Time Of Day vs Severity
  

    def time_vs_severity_chart(self):
        """Generate time vs severity chart."""
        print("\nCreating Time vs Severity Chart...")
        
        fig = self._create_figure((13, 7))
        ax = fig.add_subplot(111)
        
        sns.countplot(data=self.dataframe, x="time_of_day", hue="accident_severity",
                     palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Accident Severity by Time of Day")
        ax.set_xlabel("Time of Day", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        plt.xticks(rotation=30, ha='right')
        
        self._add_value_labels(ax)
        plt.legend(title="Severity")
        
        self._save_chart("time_vs_severity.png", folder="bar")

    
    # Vehicle Type vs Risk Band
   

    def vehicle_vs_risk_chart(self):
        """Generate vehicle vs risk band chart."""
        print("\nCreating Vehicle vs Risk Chart...")
        
        fig = self._create_figure((14, 8))
        ax = fig.add_subplot(111)
        
        sns.countplot(data=self.dataframe, x="vehicle_type", hue="risk_band",
                     palette=self.DEFAULT_PALETTE, ax=ax)
        
        self._set_title(ax, "Risk Band Distribution by Vehicle Type")
        ax.set_xlabel("Vehicle Type", fontsize=self.LABEL_SIZE)
        ax.set_ylabel("Number of Accidents", fontsize=self.LABEL_SIZE)
        plt.xticks(rotation=45, ha='right')
        
        self._add_value_labels(ax, padding=1)
        plt.legend(title="Risk Band")
        
        self._save_chart("vehicle_vs_risk_band.png", folder="bar")

    
    # Generate All Charts
    

    def generate_all(self):
        """Generate all visualizations."""
        print("\n")
        print("=" * 70)
        print("GENERATING VISUALIZATIONS")
        print("=" * 70)
        
        self.state_distribution_chart()
        self.weather_distribution_chart()
        self.vehicle_distribution_chart()
        self.gender_distribution_chart()
        self.age_group_distribution_chart()
        self.severity_distribution_chart()
        self.risk_band_chart()
        self.vehicle_pie_chart()
        self.driver_age_histogram()
        self.risk_score_histogram()
        self.speed_boxplot()
        self.season_countplot()
        self.correlation_heatmap()
        self.speed_vs_risk_scatter()
        self.season_risk_boxplot()
        self.driver_age_violin()
        self.time_vs_severity_chart()
        self.vehicle_vs_risk_chart()

        self.generate_report()
        
        print("=" * 70)
        print("ALL CHARTS GENERATED SUCCESSFULLY")
        print("=" * 70)

    def generate_report(self):
        """Generate comprehensive visualization report."""
        report_path = f"{self.REPORT_DIR}/visualization_report.txt"
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("============================================================\n")
            f.write("SMART CITY ROAD ACCIDENT ANALYTICS\n")
            f.write("VISUALIZATION REPORT\n")
            f.write("============================================================\n\n")
            
            f.write(f"Generation Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Records: {len(self.dataframe):,}\n")
            f.write(f"Total Features: {len(self.dataframe.columns)}\n")
            f.write(f"Total Charts Generated: {self.chart_count}\n\n")
            
            f.write("Chart Breakdown:\n")
            for chart_type, count in self._chart_stats.items():
                if count > 0:
                    f.write(f"  - {chart_type.title()}: {count}\n")
            
            f.write("\nOutput Directories:\n")
            f.write(f"  Charts: {self.CHARTS_DIR}/\n")
            f.write(f"  Reports: {self.REPORT_DIR}/\n")
            f.write(f"  Dashboard Assets: {self.OUTPUT_BASE}/dashboard/\n\n")
            
            f.write("Status: SUCCESS - Enterprise Grade Visualizations Complete\n")
            f.write("============================================================\n")
        
        print(f"\n[REPORT] Comprehensive report saved: {report_path}")