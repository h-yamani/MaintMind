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
    def technician_reporting_analysis(self):

        print("\nTECHNICIAN REPORTING ANALYSIS")
        print("-" * 60)

        technician_summary = (
            self.df.assign(
                note_length=self.df["technician_notes"]
                .fillna("")
                .str.split()
                .str.len()
            )
            .groupby(["technician_id", "technician_name"])
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
                average_note_length=("note_length", "mean"),
                critical_reports=(
                    "priority",
                    lambda values: (values == "Critical").sum(),
                ),
            )
            .sort_values("report_count", ascending=False)
        )

        print(technician_summary.round(2))

        plt.figure(figsize=(9, 5))

        technician_summary["report_count"].plot(kind="bar")

        plt.title("Maintenance Reports by Technician")
        plt.xlabel("Technician")
        plt.ylabel("Number of Reports")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig("figures/reports_by_technician.png")
        plt.close()
    def recurring_failure_analysis(self):

        print("\nRECURRING FAILURE ANALYSIS")
        print("-" * 60)

        recurring_failures = (
            self.df.groupby(
                ["equipment_name", "issue_type"]
            )
            .agg(
                occurrence_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
            )
            .reset_index()
            .sort_values(
                ["occurrence_count", "total_downtime"],
                ascending=False,
            )
        )

        recurring_failures = recurring_failures[
            recurring_failures["occurrence_count"] > 1
        ]

        print(recurring_failures.head(10).round(2))

        top_failures = recurring_failures.head(10).copy()

        top_failures["equipment_issue"] = (
            top_failures["equipment_name"]
            + " — "
            + top_failures["issue_type"]
        )

        plt.figure(figsize=(11, 6))

        plt.barh(
            top_failures["equipment_issue"],
            top_failures["occurrence_count"],
        )

        plt.title("Top Recurring Equipment Failures")
        plt.xlabel("Number of Occurrences")
        plt.ylabel("Equipment and Issue")
        plt.gca().invert_yaxis()
        plt.tight_layout()

        plt.savefig(
            "figures/top_recurring_failures.png"
        )

        plt.close()
    def priority_and_safety_analysis(self):

        print("\nPRIORITY AND SAFETY ANALYSIS")
        print("-" * 60)

        priority_summary = (
            self.df.groupby("priority")
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
            )
            .reindex(["Low", "Medium", "High", "Critical"])
        )

        print(priority_summary.round(2))

        safety_reports = self.df[
            self.df["issue_type"] == "Safety Concern"
        ]

        print("\nSafety-related reports:", len(safety_reports))
        print(
            "Safety-related downtime:",
            round(safety_reports["downtime_hours"].sum(), 2),
        )
        print(
            "Safety-related repair cost:",
            round(safety_reports["repair_cost"].sum(), 2),
        )

        plt.figure(figsize=(8, 5))

        priority_summary["report_count"].plot(kind="bar")

        plt.title("Maintenance Reports by Priority")
        plt.xlabel("Priority")
        plt.ylabel("Number of Reports")
        plt.xticks(rotation=0)
        plt.tight_layout()

        plt.savefig("figures/reports_by_priority.png")
        plt.close()
    def location_analysis(self):

        print("\nLOCATION ANALYSIS")
        print("-" * 60)

        location_summary = (
            self.df.groupby("location")
            .agg(
                report_count=("report_id", "count"),
                total_downtime=("downtime_hours", "sum"),
                total_repair_cost=("repair_cost", "sum"),
                critical_reports=(
                    "priority",
                    lambda values: (values == "Critical").sum(),
                ),
            )
            .sort_values("total_downtime", ascending=False)
        )

        print(location_summary.round(2))

        plt.figure(figsize=(9, 5))

        location_summary["total_downtime"].plot(kind="bar")

        plt.title("Maintenance Downtime by Location")
        plt.xlabel("Location")
        plt.ylabel("Downtime Hours")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.savefig("figures/downtime_by_location.png")
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
    profiler.technician_reporting_analysis()
    profiler.recurring_failure_analysis()
    profiler.priority_and_safety_analysis()
    profiler.location_analysis()
    
