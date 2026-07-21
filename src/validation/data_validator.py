from pathlib import Path

import pandas as pd


class MaintenanceDataValidator:

    REQUIRED_COLUMNS = [
        "report_id",
        "report_date",
        "technician_id",
        "technician_name",
        "equipment_id",
        "equipment_name",
        "equipment_type",
        "maintenance_category",
        "issue_type",
        "priority",
        "location",
        "downtime_hours",
        "repair_cost",
        "technician_notes",
    ]

    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)

    def validate(self) -> dict:
        dates = pd.to_datetime(
            self.df["report_date"],
            errors="coerce",
        )

        issue_note_mismatches = self.df[
            ~self.df.apply(
                lambda row: str(row["issue_type"])
                in str(row["technician_notes"]),
                axis=1,
            )
        ]

        results = {
            "Rows": len(self.df),
            "Columns": len(self.df.columns),
            "Missing required columns": len(
                [
                    column
                    for column in self.REQUIRED_COLUMNS
                    if column not in self.df.columns
                ]
            ),
            "Missing values": int(self.df.isna().sum().sum()),
            "Duplicate report IDs": int(
                self.df["report_id"].duplicated().sum()
            ),
            "Duplicate complete records": int(
                self.df.duplicated().sum()
            ),
            "Invalid dates": int(dates.isna().sum()),
            "Negative downtime values": int(
                (self.df["downtime_hours"] < 0).sum()
            ),
            "Negative repair costs": int(
                (self.df["repair_cost"] < 0).sum()
            ),
            "Technician ID mapping errors": int(
                (
                    self.df.groupby("technician_id")[
                        "technician_name"
                    ].nunique()
                    > 1
                ).sum()
            ),
            "Equipment name mapping errors": int(
                (
                    self.df.groupby("equipment_id")[
                        "equipment_name"
                    ].nunique()
                    > 1
                ).sum()
            ),
            "Equipment type mapping errors": int(
                (
                    self.df.groupby("equipment_id")[
                        "equipment_type"
                    ].nunique()
                    > 1
                ).sum()
            ),
            "Issue-note mismatches": len(issue_note_mismatches),
        }

        return results

    def print_report(self, results: dict) -> None:
        print("=" * 60)
        print("MAINTMIND DATA VALIDATION REPORT")
        print("=" * 60)

        for check, value in results.items():
            print(f"{check}: {value}")

    def save_markdown_report(
        self,
        results: dict,
        output_path: str,
    ) -> None:
        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        error_checks = list(results.values())[2:]
        status = (
            "PASS"
            if all(value == 0 for value in error_checks)
            else "REVIEW REQUIRED"
        )

        lines = [
            "# MaintMind Data Validation Report",
            "",
            f"**Overall status:** {status}",
            "",
            "| Validation check | Result |",
            "|---|---:|",
        ]

        for check, value in results.items():
            lines.append(f"| {check} | {value} |")

        lines.extend(
            [
                "",
                "## Conclusion",
                "",
                (
                    "The maintenance dataset passed all implemented "
                    "data-quality checks."
                    if status == "PASS"
                    else "The dataset contains issues requiring review."
                ),
            ]
        )

        Path(output_path).write_text(
            "\n".join(lines),
            encoding="utf-8",
        )

        print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    validator = MaintenanceDataValidator(
        "data/maintenance_reports.csv"
    )

    validation_results = validator.validate()
    validator.print_report(validation_results)
    validator.save_markdown_report(
        validation_results,
        "reports/data_validation_report.md",
    )
