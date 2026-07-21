import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class MaintenanceOperationsProfiler:

    def __init__(self, data_path: str):

        self.df = pd.read_csv(data_path)

        self.df["report_date"] = pd.to_datetime(
        self.df["report_date"]
        )
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
    def monthly_report_analysis(self):

        print("\nMONTHLY REPORT VOLUME")
        print("-" * 60)

        monthly_counts = (
            self.df
            .set_index("report_date")
            .resample("M")
            .size()
        )

        print(monthly_counts)

        plt.figure(figsize=(10, 5))

        monthly_counts.plot(
            kind="line",
            marker="o",
        )

        plt.title("Monthly Maintenance Report Volume")
        plt.xlabel("Month")
        plt.ylabel("Number of Reports")
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(
            "figures/monthly_report_volume.png"
        )

        plt.close()
    def equipment_workload_analysis(self):

        print("\nEQUIPMENT WORKLOAD ANALYSIS")
        print("-" * 60)

        equipment_summary = (
            self.df.groupby("equipment_name")
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
            )
            .sort_values("report_count", ascending=False)
        )

        print(equipment_summary.round(2))

        plt.figure(figsize=(10, 5))

        equipment_summary["report_count"].plot(
            kind="bar"
        )

        plt.title("Maintenance Reports by Equipment")
        plt.xlabel("Equipment")
        plt.ylabel("Number of Reports")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig(
            "figures/equipment_maintenance_workload.png"
        )

        plt.close()
    def equipment_workload_analysis(self):

        print("\nEQUIPMENT WORKLOAD ANALYSIS")
        print("-" * 60)

        equipment_summary = (
            self.df.groupby("equipment_name")
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
            )
            .sort_values("report_count", ascending=False)
        )

        print(equipment_summary.round(2))

        plt.figure(figsize=(10, 5))

        equipment_summary["report_count"].plot(kind="bar")

        plt.title("Maintenance Reports by Equipment")
        plt.xlabel("Equipment")
        plt.ylabel("Number of Reports")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig(
            "figures/equipment_maintenance_workload.png"
        )

        plt.close() 
    def failure_analysis(self):

        print("\nFAILURE ANALYSIS")
        print("-" * 60)

        failure_summary = (
            self.df.groupby("issue_type")
            .agg(
                failure_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
            )
            .sort_values("failure_count", ascending=False)
        )

        print(failure_summary.round(2))

        plt.figure(figsize=(9, 5))

        failure_summary["failure_count"].plot(kind="bar")

        plt.title("Maintenance Failures by Issue Type")
        plt.xlabel("Issue Type")
        plt.ylabel("Number of Reports")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig("figures/issue_type_distribution.png")
        plt.close()
    def downtime_and_cost_analysis(self):

        print("\nDOWNTIME AND COST ANALYSIS")
        print("-" * 60)

        category_summary = (
            self.df.groupby("maintenance_category")
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                average_downtime=("downtime_hours", "mean"),
                total_repair_cost=("repair_cost", "sum"),
                average_repair_cost=("repair_cost", "mean"),
            )
            .sort_values("total_downtime", ascending=False)
        )

        print(category_summary.round(2))

        plt.figure(figsize=(10, 5))

        category_summary["total_downtime"].plot(kind="bar")

        plt.title("Total Downtime by Maintenance Category")
        plt.xlabel("Maintenance Category")
        plt.ylabel("Downtime Hours")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig(
            "figures/downtime_by_maintenance_category.png"
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
    profiler.monthly_report_analysis()
    profiler.equipment_workload_analysis()
    profiler.failure_analysis()
    profiler.downtime_and_cost_analysis()
    
