import pandas as pd


class MaintenanceOperationsProfiler:

    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)

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

        print(
	    self.df["maintenance_category"]
	    .value_counts()
        )

if __name__ == "__main__":

    profiler = MaintenanceOperationsProfiler(
        "data/maintenance_reports.csv"
    )

    profiler.dataset_summary()

    profiler.missing_values_report()

    profiler.duplicate_report_analysis()

    profiler.maintenance_category_analysis()
