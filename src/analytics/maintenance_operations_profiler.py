from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd


LOGGER = logging.getLogger(__name__)


class MaintenanceOperationsProfiler:
    """Profile maintenance operations data and generate analytical figures."""

    BASE_REQUIRED_COLUMNS = {
        "report_id",
        "report_date",
    }

    PROVENANCE_COLUMNS = {
        "source_system",
        "source_dataset",
        "source_record_id",
        "is_synthetic",
        "is_augmented",
        "licence",
        "schema_version",
    }

    PRIORITY_ORDER = [
        "Low",
        "Medium",
        "High",
        "Critical",
    ]

    def __init__(
        self,
        data_path: str | Path,
        figures_dir: str | Path = "figures",
        source_dataset: str | None = None,
    ) -> None:
        """Load maintenance data and prepare the output directory."""

        self.data_path = Path(data_path)
        self.figures_dir = Path(figures_dir)
        self.source_dataset = source_dataset

        self.figures_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.df = self._load_data()

        if source_dataset is not None:
            self.df = self._filter_source_dataset(
                source_dataset
            )

        self.figure_prefix = self._create_figure_prefix()

        self._warn_about_mixed_sources()

    def _load_data(self) -> pd.DataFrame:
        """Load and minimally validate the dataset."""

        if not self.data_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.data_path}"
            )

        dataframe = pd.read_csv(self.data_path)

        missing_columns = (
            self.BASE_REQUIRED_COLUMNS
            - set(dataframe.columns)
        )

        if missing_columns:
            raise ValueError(
                "Dataset is missing required columns: "
                + ", ".join(sorted(missing_columns))
            )

        dataframe["report_date"] = pd.to_datetime(
            dataframe["report_date"],
            errors="raise",
        )

        numeric_columns = [
            "downtime_hours",
            "repair_cost",
        ]

        for column in numeric_columns:
            if column in dataframe.columns:
                dataframe[column] = pd.to_numeric(
                    dataframe[column],
                    errors="raise",
                )

        for column in ["is_synthetic", "is_augmented"]:
            if column in dataframe.columns:
                dataframe[column] = (
                    dataframe[column]
                    .astype(str)
                    .str.strip()
                    .str.lower()
                    .map(
                        {
                            "true": True,
                            "false": False,
                            "1": True,
                            "0": False,
                        }
                    )
                )

                if dataframe[column].isna().any():
                    raise ValueError(
                        f"Column '{column}' contains "
                        "invalid boolean values."
                    )

        return dataframe

    def _filter_source_dataset(
        self,
        source_dataset: str,
    ) -> pd.DataFrame:
        """Filter records to one explicitly selected source."""

        if "source_dataset" not in self.df.columns:
            raise ValueError(
                "Cannot filter by source because "
                "'source_dataset' is missing."
            )

        filtered_data = self.df[
            self.df["source_dataset"] == source_dataset
        ].copy()

        if filtered_data.empty:
            available_sources = sorted(
                self.df["source_dataset"]
                .dropna()
                .astype(str)
                .unique()
            )

            raise ValueError(
                f"No records found for source "
                f"'{source_dataset}'. Available sources: "
                f"{available_sources}"
            )

        return filtered_data

    def _warn_about_mixed_sources(self) -> None:
        """Warn when several datasets are analysed together."""

        if "source_dataset" not in self.df.columns:
            LOGGER.warning(
                "Provenance columns are not present. "
                "The dataset should be upgraded before "
                "real-data ingestion."
            )
            return

        source_count = (
            self.df["source_dataset"]
            .dropna()
            .nunique()
        )

        if source_count > 1 and self.source_dataset is None:
            LOGGER.warning(
                "Multiple source datasets are loaded. "
                "Use --source-dataset for source-specific "
                "business analysis."
            )

    def _create_figure_prefix(self) -> str:
        """Create a filename prefix for source-specific figures."""

        if self.source_dataset is None:
            return ""

        safe_name = "".join(
            character.lower()
            if character.isalnum()
            else "_"
            for character in self.source_dataset
        ).strip("_")

        return f"{safe_name}_"

    def _figure_path(self, filename: str) -> Path:
        """Return the complete output path for a figure."""

        return self.figures_dir / (
            self.figure_prefix + filename
        )

    @staticmethod
    def _print_section(title: str) -> None:
        """Print a consistent analysis section header."""

        print(f"\n{title}")
        print("-" * 60)

    def _has_columns(
        self,
        columns: Iterable[str],
        analysis_name: str,
    ) -> bool:
        """Check whether columns required by an analysis exist."""

        missing_columns = sorted(
            set(columns) - set(self.df.columns)
        )

        if not missing_columns:
            return True

        self._print_section(analysis_name)
        print(
            "Analysis skipped. Missing columns: "
            + ", ".join(missing_columns)
        )

        LOGGER.warning(
            "%s skipped because columns are missing: %s",
            analysis_name,
            ", ".join(missing_columns),
        )

        return False

    def _save_bar_chart(
        self,
        values: pd.Series,
        filename: str,
        title: str,
        xlabel: str,
        ylabel: str,
        horizontal: bool = False,
        rotation: int = 45,
        figsize: tuple[int, int] = (10, 5),
    ) -> None:
        """Save a standard bar chart."""

        plot_values = values.copy()
        plot_values.index = plot_values.index.map(str)

        figure, axis = plt.subplots(
            figsize=figsize
        )

        if horizontal:
            plot_values.plot(
                kind="barh",
                ax=axis,
            )
        else:
            plot_values.plot(
                kind="bar",
                ax=axis,
            )
            axis.tick_params(
                axis="x",
                rotation=rotation,
            )

        axis.set_title(title)
        axis.set_xlabel(xlabel)
        axis.set_ylabel(ylabel)

        figure.tight_layout()

        figure.savefig(
            self._figure_path(filename),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(figure)

    def dataset_summary(self) -> dict[str, object]:
        """Print and return a high-level dataset summary."""

        print("=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)

        summary: dict[str, object] = {
            "total_reports": len(self.df),
            "total_columns": len(self.df.columns),
            "date_start": self.df["report_date"].min(),
            "date_end": self.df["report_date"].max(),
        }

        print(
            f"Total Reports: "
            f"{summary['total_reports']}"
        )
        print(
            f"Columns: "
            f"{summary['total_columns']}"
        )
        print(
            f"Date Range: "
            f"{summary['date_start'].date()} to "
            f"{summary['date_end'].date()}"
        )

        if "downtime_hours" in self.df.columns:
            total_downtime = (
                self.df["downtime_hours"].sum()
            )
            summary["total_downtime"] = total_downtime

            print(
                f"Total Downtime: "
                f"{total_downtime:,.1f} hours"
            )

        if "repair_cost" in self.df.columns:
            total_repair_cost = (
                self.df["repair_cost"].sum()
            )
            summary[
                "total_repair_cost"
            ] = total_repair_cost

            print(
                f"Total Repair Cost: "
                f"${total_repair_cost:,.2f}"
            )

        return summary

    def provenance_analysis(self) -> pd.DataFrame:
        """Analyse source provenance and synthetic-data status."""

        self._print_section("DATA PROVENANCE ANALYSIS")

        missing_columns = sorted(
            self.PROVENANCE_COLUMNS
            - set(self.df.columns)
        )

        if missing_columns:
            print(
                "Missing provenance columns: "
                + ", ".join(missing_columns)
            )

            return pd.DataFrame()

        provenance_summary = (
            self.df.groupby(
                [
                    "source_system",
                    "source_dataset",
                    "is_synthetic",
                    "is_augmented",
                    "schema_version",
                ],
                dropna=False,
            )
            .agg(
                record_count=("report_id", "count"),
                earliest_record=(
                    "report_date",
                    "min",
                ),
                latest_record=(
                    "report_date",
                    "max",
                ),
            )
            .reset_index()
        )

        duplicate_source_records = (
            self.df.duplicated(
                subset=[
                    "source_dataset",
                    "source_record_id",
                ]
            ).sum()
        )

        print(provenance_summary.to_string(index=False))
        print(
            "\nDuplicate source identifiers:",
            duplicate_source_records,
        )

        real_records = (
            ~self.df["is_synthetic"]
        ).sum()

        synthetic_records = (
            self.df["is_synthetic"]
        ).sum()

        augmented_records = (
            self.df["is_augmented"]
        ).sum()

        print("Real records:", int(real_records))
        print(
            "Synthetic records:",
            int(synthetic_records),
        )
        print(
            "Augmented records:",
            int(augmented_records),
        )

        return provenance_summary

    def missing_values_report(self) -> pd.Series:
        """Print and return missing-value counts."""

        self._print_section("MISSING VALUES")

        missing_values = self.df.isna().sum()

        print(missing_values)

        return missing_values

    def duplicate_report_analysis(self) -> int:
        """Print and return duplicate-record counts."""

        self._print_section("DUPLICATE REPORTS")

        duplicate_records = int(
            self.df.duplicated().sum()
        )

        duplicate_report_ids = int(
            self.df["report_id"].duplicated().sum()
        )

        print(
            "Duplicate complete records:",
            duplicate_records,
        )
        print(
            "Duplicate report IDs:",
            duplicate_report_ids,
        )

        return duplicate_records

    def maintenance_category_analysis(
        self,
    ) -> pd.Series:
        """Analyse maintenance category volume."""

        analysis_name = (
            "MAINTENANCE CATEGORY ANALYSIS"
        )

        if not self._has_columns(
            ["maintenance_category"],
            analysis_name,
        ):
            return pd.Series(dtype="int64")

        self._print_section(analysis_name)

        category_counts = (
            self.df["maintenance_category"]
            .value_counts()
        )

        print(category_counts)

        self._save_bar_chart(
            values=category_counts,
            filename=(
                "maintenance_category_distribution.png"
            ),
            title=(
                "Maintenance Category Distribution"
            ),
            xlabel="Maintenance Category",
            ylabel="Number of Reports",
        )

        return category_counts

    def monthly_report_analysis(self) -> pd.Series:
        """Analyse monthly report volume."""

        self._print_section(
            "MONTHLY REPORT VOLUME"
        )

        monthly_counts = (
            self.df.assign(
                report_month=(
                    self.df["report_date"]
                    .dt.to_period("M")
                    .astype(str)
                )
            )
            .groupby("report_month")
            .size()
        )

        print(monthly_counts)

        figure, axis = plt.subplots(
            figsize=(10, 5)
        )

        axis.plot(
            monthly_counts.index,
            monthly_counts.values,
            marker="o",
        )

        axis.set_title(
            "Monthly Maintenance Report Volume"
        )
        axis.set_xlabel("Month")
        axis.set_ylabel("Number of Reports")
        axis.tick_params(
            axis="x",
            rotation=45,
        )
        axis.grid(True)

        figure.tight_layout()

        figure.savefig(
            self._figure_path(
                "monthly_report_volume.png"
            ),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(figure)

        return monthly_counts

    def equipment_workload_analysis(
        self,
    ) -> pd.DataFrame:
        """Analyse maintenance workload by equipment."""

        analysis_name = (
            "EQUIPMENT WORKLOAD ANALYSIS"
        )

        required_columns = [
            "equipment_name",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        equipment_summary = (
            self.df.groupby("equipment_name")
            .agg(
                report_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
            )
            .sort_values(
                "report_count",
                ascending=False,
            )
        )

        print(equipment_summary.round(2))

        self._save_bar_chart(
            values=(
                equipment_summary[
                    "report_count"
                ]
            ),
            filename=(
                "equipment_maintenance_workload.png"
            ),
            title=(
                "Maintenance Reports by Equipment"
            ),
            xlabel="Equipment",
            ylabel="Number of Reports",
        )

        return equipment_summary

    def failure_analysis(self) -> pd.DataFrame:
        """Analyse issue frequency, downtime, and cost."""

        analysis_name = "FAILURE ANALYSIS"

        required_columns = [
            "issue_type",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        failure_summary = (
            self.df.groupby("issue_type")
            .agg(
                failure_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
            )
            .sort_values(
                "failure_count",
                ascending=False,
            )
        )

        print(failure_summary.round(2))

        self._save_bar_chart(
            values=(
                failure_summary[
                    "failure_count"
                ]
            ),
            filename=(
                "issue_type_distribution.png"
            ),
            title=(
                "Maintenance Failures by Issue Type"
            ),
            xlabel="Issue Type",
            ylabel="Number of Reports",
        )

        return failure_summary

    def downtime_and_cost_analysis(
        self,
    ) -> pd.DataFrame:
        """Analyse downtime and repair cost by category."""

        analysis_name = (
            "DOWNTIME AND COST ANALYSIS"
        )

        required_columns = [
            "maintenance_category",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        category_summary = (
            self.df.groupby(
                "maintenance_category"
            )
            .agg(
                report_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                average_downtime=(
                    "downtime_hours",
                    "mean",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
                average_repair_cost=(
                    "repair_cost",
                    "mean",
                ),
            )
            .sort_values(
                "total_downtime",
                ascending=False,
            )
        )

        print(category_summary.round(2))

        self._save_bar_chart(
            values=(
                category_summary[
                    "total_downtime"
                ]
            ),
            filename=(
                "downtime_by_maintenance_category.png"
            ),
            title=(
                "Total Downtime by Maintenance Category"
            ),
            xlabel="Maintenance Category",
            ylabel="Downtime Hours",
        )

        return category_summary

    def technician_reporting_analysis(
        self,
    ) -> pd.DataFrame:
        """Analyse technician workload and note quality."""

        analysis_name = (
            "TECHNICIAN REPORTING ANALYSIS"
        )

        required_columns = [
            "technician_id",
            "technician_name",
            "technician_notes",
            "downtime_hours",
            "repair_cost",
            "priority",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        technician_summary = (
            self.df.assign(
                note_length=(
                    self.df["technician_notes"]
                    .fillna("")
                    .str.split()
                    .str.len()
                )
            )
            .groupby(
                [
                    "technician_id",
                    "technician_name",
                ]
            )
            .agg(
                report_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
                average_note_length=(
                    "note_length",
                    "mean",
                ),
                critical_reports=(
                    "priority",
                    lambda values: (
                        values == "Critical"
                    ).sum(),
                ),
            )
            .sort_values(
                "report_count",
                ascending=False,
            )
        )

        print(technician_summary.round(2))

        chart_values = (
            technician_summary[
                "report_count"
            ].copy()
        )

        chart_values.index = [
            technician_name
            for _, technician_name
            in chart_values.index
        ]

        self._save_bar_chart(
            values=chart_values,
            filename=(
                "reports_by_technician.png"
            ),
            title=(
                "Maintenance Reports by Technician"
            ),
            xlabel="Technician",
            ylabel="Number of Reports",
        )

        return technician_summary

    def recurring_failure_analysis(
        self,
    ) -> pd.DataFrame:
        """Identify repeated equipment and issue combinations."""

        analysis_name = (
            "RECURRING FAILURE ANALYSIS"
        )

        required_columns = [
            "equipment_name",
            "issue_type",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        recurring_failures = (
            self.df.groupby(
                [
                    "equipment_name",
                    "issue_type",
                ]
            )
            .agg(
                occurrence_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
            )
            .reset_index()
            .query("occurrence_count > 1")
            .sort_values(
                [
                    "occurrence_count",
                    "total_downtime",
                ],
                ascending=False,
            )
        )

        print(
            recurring_failures
            .head(10)
            .round(2)
        )

        if recurring_failures.empty:
            print(
                "No recurring equipment failures "
                "were identified."
            )
            return recurring_failures

        top_failures = (
            recurring_failures
            .head(10)
            .copy()
        )

        top_failures["equipment_issue"] = (
            top_failures["equipment_name"]
            + " — "
            + top_failures["issue_type"]
        )

        figure, axis = plt.subplots(
            figsize=(11, 6)
        )

        axis.barh(
            top_failures["equipment_issue"],
            top_failures[
                "occurrence_count"
            ],
        )

        axis.set_title(
            "Top Recurring Equipment Failures"
        )
        axis.set_xlabel(
            "Number of Occurrences"
        )
        axis.set_ylabel(
            "Equipment and Issue"
        )
        axis.invert_yaxis()

        figure.tight_layout()

        figure.savefig(
            self._figure_path(
                "top_recurring_failures.png"
            ),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(figure)

        return recurring_failures

    def priority_and_safety_analysis(
        self,
    ) -> pd.DataFrame:
        """Analyse maintenance priority and safety exposure."""

        analysis_name = (
            "PRIORITY AND SAFETY ANALYSIS"
        )

        required_columns = [
            "priority",
            "issue_type",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        priority_summary = (
            self.df.groupby("priority")
            .agg(
                report_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
            )
            .reindex(self.PRIORITY_ORDER)
            .fillna(0)
        )

        print(priority_summary.round(2))

        safety_reports = self.df[
            self.df["issue_type"]
            == "Safety Concern"
        ]

        print(
            "\nSafety-related reports:",
            len(safety_reports),
        )
        print(
            "Safety-related downtime:",
            round(
                safety_reports[
                    "downtime_hours"
                ].sum(),
                2,
            ),
        )
        print(
            "Safety-related repair cost:",
            round(
                safety_reports[
                    "repair_cost"
                ].sum(),
                2,
            ),
        )

        self._save_bar_chart(
            values=(
                priority_summary[
                    "report_count"
                ]
            ),
            filename=(
                "reports_by_priority.png"
            ),
            title=(
                "Maintenance Reports by Priority"
            ),
            xlabel="Priority",
            ylabel="Number of Reports",
            rotation=0,
            figsize=(8, 5),
        )

        return priority_summary

    def location_analysis(self) -> pd.DataFrame:
        """Analyse maintenance workload by location."""

        analysis_name = "LOCATION ANALYSIS"

        required_columns = [
            "location",
            "priority",
            "downtime_hours",
            "repair_cost",
        ]

        if not self._has_columns(
            required_columns,
            analysis_name,
        ):
            return pd.DataFrame()

        self._print_section(analysis_name)

        location_summary = (
            self.df.groupby("location")
            .agg(
                report_count=(
                    "report_id",
                    "count",
                ),
                total_downtime=(
                    "downtime_hours",
                    "sum",
                ),
                total_repair_cost=(
                    "repair_cost",
                    "sum",
                ),
                critical_reports=(
                    "priority",
                    lambda values: (
                        values == "Critical"
                    ).sum(),
                ),
            )
            .sort_values(
                "total_downtime",
                ascending=False,
            )
        )

        print(location_summary.round(2))

        self._save_bar_chart(
            values=(
                location_summary[
                    "total_downtime"
                ]
            ),
            filename=(
                "downtime_by_location.png"
            ),
            title=(
                "Maintenance Downtime by Location"
            ),
            xlabel="Location",
            ylabel="Downtime Hours",
        )

        return location_summary

    def run_all(self) -> None:
        """Run every available profiling analysis."""

        self.dataset_summary()
        self.provenance_analysis()
        self.missing_values_report()
        self.duplicate_report_analysis()
        self.maintenance_category_analysis()
        self.monthly_report_analysis()
        self.equipment_workload_analysis()
        self.failure_analysis()
        self.downtime_and_cost_analysis()
        self.technician_reporting_analysis()
        self.recurring_failure_analysis()
        self.priority_and_safety_analysis()
        self.location_analysis()


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Profile maintenance operations data "
            "and generate analytical figures."
        )
    )

    parser.add_argument(
        "--data-path",
        default="data/maintenance_reports.csv",
        help="Path to the maintenance CSV file.",
    )

    parser.add_argument(
        "--figures-dir",
        default="figures",
        help="Directory used to save figures.",
    )

    parser.add_argument(
        "--source-dataset",
        default=None,
        help=(
            "Optional source dataset to analyse "
            "without combining unrelated sources."
        ),
    )

    return parser.parse_args()


def main() -> None:
    """Run the maintenance operations profiler."""

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
    )

    arguments = parse_arguments()

    profiler = MaintenanceOperationsProfiler(
        data_path=arguments.data_path,
        figures_dir=arguments.figures_dir,
        source_dataset=arguments.source_dataset,
    )

    profiler.run_all()


if __name__ == "__main__":
    main()