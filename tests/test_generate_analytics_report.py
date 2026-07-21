from pathlib import Path

import pandas as pd

from src.analytics.generate_analytics_report import (
    generate_report,
    load_data,
)


def sample_maintenance_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "report_id": ["REP001", "REP002"],
            "report_date": ["2025-01-01", "2025-01-02"],
            "equipment_name": [
                "CAT320 Excavator",
                "CAT320 Excavator",
            ],
            "issue_type": [
                "Bearing Wear",
                "Bearing Wear",
            ],
            "priority": ["Critical", "High"],
            "location": ["Auckland", "Auckland"],
            "downtime_hours": [5.0, 7.0],
            "repair_cost": [1000.0, 1500.0],
        }
    )


def test_load_data_parses_report_dates(tmp_path: Path) -> None:
    csv_path = tmp_path / "maintenance.csv"
    sample_maintenance_data().to_csv(csv_path, index=False)

    dataframe = load_data(csv_path)

    assert len(dataframe) == 2
    assert pd.api.types.is_datetime64_any_dtype(
        dataframe["report_date"]
    )


def test_load_data_raises_for_missing_file(
    tmp_path: Path,
) -> None:
    missing_path = tmp_path / "missing.csv"

    try:
        load_data(missing_path)
    except FileNotFoundError as error:
        assert "Dataset not found" in str(error)
    else:
        raise AssertionError("Expected FileNotFoundError")


def test_generate_report_contains_key_findings() -> None:
    dataframe = sample_maintenance_data()
    dataframe["report_date"] = pd.to_datetime(
        dataframe["report_date"]
    )

    report = generate_report(dataframe)

    assert "2 maintenance reports" in report
    assert "12.0 hours" in report
    assert "$2,500.00" in report
    assert "CAT320 Excavator" in report
    assert "Bearing Wear" in report
    assert "Auckland" in report
    assert "synthetic" in report

