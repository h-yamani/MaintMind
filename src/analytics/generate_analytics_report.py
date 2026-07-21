from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/maintenance_reports.csv")
REPORT_PATH = Path("reports/maintenance_analytics_report.md")


def load_data(path: Path) -> pd.DataFrame:
    """Load and prepare maintenance data."""

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    dataframe = pd.read_csv(path)
    dataframe["report_date"] = pd.to_datetime(
        dataframe["report_date"],
        errors="raise",
    )

    return dataframe


def generate_report(dataframe: pd.DataFrame) -> str:
    """Generate a Markdown maintenance analytics report."""

    total_reports = len(dataframe)
    total_downtime = dataframe["downtime_hours"].sum()
    total_cost = dataframe["repair_cost"].sum()
    average_cost = dataframe["repair_cost"].mean()

    critical_reports = (
        dataframe["priority"] == "Critical"
    ).sum()

    top_equipment = (
        dataframe.groupby("equipment_name")["downtime_hours"]
        .sum()
        .sort_values(ascending=False)
    )

    top_issues = (
        dataframe.groupby("issue_type")
        .agg(
            occurrences=("report_id", "count"),
            downtime_hours=("downtime_hours", "sum"),
            repair_cost=("repair_cost", "sum"),
        )
        .sort_values("occurrences", ascending=False)
    )

    location_summary = (
        dataframe.groupby("location")
        .agg(
            reports=("report_id", "count"),
            downtime_hours=("downtime_hours", "sum"),
            repair_cost=("repair_cost", "sum"),
        )
        .sort_values("downtime_hours", ascending=False)
    )

    recurring_failures = (
        dataframe.groupby(["equipment_name", "issue_type"])
        .agg(
            occurrences=("report_id", "count"),
            downtime_hours=("downtime_hours", "sum"),
            repair_cost=("repair_cost", "sum"),
        )
        .reset_index()
        .query("occurrences > 1")
        .sort_values(
            ["occurrences", "downtime_hours"],
            ascending=False,
        )
        .head(5)
    )

    report = f"""# MaintMind Maintenance Analytics Report

## Executive Summary

The dataset contains **{total_reports} maintenance reports**.

- Total recorded downtime: **{total_downtime:,.1f} hours**
- Total repair cost: **${total_cost:,.2f}**
- Average repair cost per report: **${average_cost:,.2f}**
- Critical-priority reports: **{critical_reports}**

## Equipment Risk

The equipment with the greatest accumulated downtime was
**{top_equipment.index[0]}**, with
**{top_equipment.iloc[0]:,.1f} downtime hours**.

### Equipment downtime ranking

{top_equipment.round(2).to_frame("downtime_hours").to_markdown()}

## Failure Patterns

The most frequently reported issue was
**{top_issues.index[0]}**, with
**{int(top_issues.iloc[0]["occurrences"])} occurrences**.

{top_issues.round(2).to_markdown()}

## Location Performance

The location with the greatest accumulated downtime was
**{location_summary.index[0]}**, with
**{location_summary.iloc[0]["downtime_hours"]:,.1f} hours**.

{location_summary.round(2).to_markdown()}

## Top Recurring Failures

{recurring_failures.round(2).to_markdown(index=False)}

## Recommended Automation Opportunities

1. Automatically flag repeated equipment–issue combinations.
2. Notify operations teams when critical reports are submitted.
3. Prioritise equipment with high cumulative downtime.
4. Trigger preventive-maintenance reviews after repeated failures.
5. Generate weekly summaries of cost, downtime, and safety risks.

## Assumptions and Limitations

- This dataset is synthetic and does not represent a real organisation.
- Maintenance categories, costs, priorities, and failures are simulated.
- Results demonstrate analytical and engineering capability rather than operational truth.
- Predictive conclusions should not be used without real historical maintenance data.
"""

    return report


def main() -> None:
    """Create and save the analytics report."""

    dataframe = load_data(DATA_PATH)
    report = generate_report(dataframe)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")

    print(f"Report saved to {REPORT_PATH}")


if __name__ == "__main__":
    main()
