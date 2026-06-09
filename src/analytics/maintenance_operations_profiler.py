import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class MaintenanceOperationsProfiler:

    def __init__(self, data_path: str):

        self.df = pd.read_csv(data_path)

        Path("figures").mkdir(exist_ok=True)
        
    def dataset_summary(self):

        print("=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)

        print(f"Total Reports: {len(self.df)}")
        print(f"Columns: {len(self.df.columns)}")

    def missing_values_report(self):

        print("\nMISSING VALUES")
        print("-" * 60)

        print(self.df.isnull().sum())

    def duplicate_report_analysis(self):

        print("\nDUPLICATE REPORTS")
        print("-" * 60)

        print(self.df.duplicated().sum())
    
    def maintenance_category_analysis(self):

	    print("\nMAINTENANCE CATEGORY ANALYSIS")
	    print("-" * 60)

	    category_counts = (
		self.df["maintenance_category"]
		.value_counts()
	    )

	    print(category_counts)

	    plt.figure(figsize=(8, 5))

	    category_counts.plot(
		kind="bar"
	    )

	    plt.title(
		"Maintenance Category Distribution"
	    )

	    plt.xlabel(
		"Maintenance Category"
	    )

	    plt.ylabel(
		"Number of Reports"
	    )

	    plt.tight_layout()

	    plt.savefig(
		"figures/maintenance_category_distribution.png"
	    )

	    plt.close()

if __name__ == "__main__":

    profiler = MaintenanceOperationsProfiler(
        "data/maintenance_reports.csv"
    )

    profiler.dataset_summary()

    profiler.missing_values_report()

    profiler.duplicate_report_analysis()

    profiler.maintenance_category_analysis()
