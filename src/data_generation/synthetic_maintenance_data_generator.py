from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

RANDOM_SEED = 42
REPORT_COUNT = 100

START_DATE = datetime(2025, 1, 1)

OUTPUT_PATH = Path("data/maintenance_reports.csv")

SOURCE_SYSTEM = "maintmind_generator"
SOURCE_DATASET = "maintmind_synthetic_v1"
SCHEMA_VERSION = "1.0.0"
DATA_LICENCE = "CC0-1.0"

# Fixed because this dataset will be frozen as a
# reproducible testing and demonstration fixture.
INGESTION_TIMESTAMP = "2026-07-21T00:00:00Z"


TECHNICIANS = [
    ("TECH001", "John Smith"),
    ("TECH002", "Sarah Wilson"),
    ("TECH003", "Mike Brown"),
    ("TECH004", "David Taylor"),
    ("TECH005", "Emma Johnson"),
]

EQUIPMENT = [
    (
        "EQ001",
        "CAT320 Excavator",
        "Excavator",
    ),
    (
        "EQ002",
        "Komatsu D65",
        "Bulldozer",
    ),
    (
        "EQ003",
        "Hitachi ZX200",
        "Excavator",
    ),
    (
        "EQ004",
        "Hydraulic Press A",
        "Hydraulic System",
    ),
    (
        "EQ005",
        "Generator G1",
        "Generator",
    ),
    (
        "EQ006",
        "Forklift F3",
        "Forklift",
    ),
]

CATEGORIES = [
    "Hydraulic",
    "Diesel",
    "Electrical",
    "Inspection",
    "Fabrication",
    "Preventive Maintenance",
]

ISSUES = [
    "Hydraulic Leak",
    "Bearing Wear",
    "Electrical Fault",
    "Pressure Loss",
    "Overheating",
    "Safety Concern",
]

ISSUE_ACTIONS = {
    "Hydraulic Leak": [
        ("Replaced the damaged hydraulic hose and tightened the coupling"),
        ("Replaced the leaking seal and cleaned the affected area"),
        ("Tightened loose fittings and completed a pressure test"),
    ],
    "Bearing Wear": [
        ("Replaced the worn bearing and lubricated the assembly"),
        ("Adjusted the bearing alignment and tested rotation"),
        ("Removed the damaged bearing and installed a replacement"),
    ],
    "Electrical Fault": [
        ("Repaired damaged wiring and tested the electrical circuit"),
        ("Replaced the faulty relay and verified normal operation"),
        ("Cleaned the electrical connections and secured loose terminals"),
    ],
    "Pressure Loss": [
        ("Adjusted the pressure regulator and tested system pressure"),
        "Replaced the faulty pressure valve",
        ("Inspected the system for leaks and restored operating pressure"),
    ],
    "Overheating": [
        ("Cleaned the cooling system and checked coolant levels"),
        "Replaced the damaged cooling fan",
        ("Cleared blocked ventilation and tested operating temperature"),
    ],
    "Safety Concern": [
        ("Secured the unsafe component and completed a safety inspection"),
        "Replaced the damaged safety guard",
        ("Isolated the equipment and corrected the identified hazard"),
    ],
}

FOLLOW_UP_ACTIONS = [
    ("Monitor the equipment during the next operating shift"),
    ("Schedule a follow-up inspection within two weeks"),
    ("Review the issue during the next preventive maintenance service"),
    ("No further action is required unless the issue returns"),
    ("Inspect related components for similar wear"),
]

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical",
]

LOCATIONS = [
    "Auckland",
    "Hamilton",
    "Tauranga",
    "Wellington",
]


def create_technician_note(
    equipment_name: str,
    issue: str,
    repair_action: str,
    follow_up: str,
) -> str:
    """Create a varied maintenance note."""

    note_templates = [
        (
            f"Inspection of {equipment_name} "
            f"identified {issue}. "
            f"{repair_action}. {follow_up}."
        ),
        (
            f"Technician attended {equipment_name} "
            f"following a reported {issue}. "
            f"{repair_action}. Equipment was tested "
            f"before returning to service. "
            f"{follow_up}."
        ),
        (
            f"{issue} was detected during "
            f"maintenance of {equipment_name}. "
            f"{repair_action}. Operational checks "
            f"were completed successfully. "
            f"{follow_up}."
        ),
    ]

    return random.choice(note_templates)


def generate_maintenance_reports(
    report_count: int = REPORT_COUNT,
) -> pd.DataFrame:
    """Generate reproducible synthetic maintenance reports."""

    if report_count <= 0:
        raise ValueError("report_count must be greater than zero.")

    random.seed(RANDOM_SEED)

    reports: list[dict[str, object]] = []

    for index in range(report_count):
        report_id = f"REP{index + 1:03d}"

        (
            equipment_id,
            equipment_name,
            equipment_type,
        ) = random.choice(EQUIPMENT)

        (
            technician_id,
            technician_name,
        ) = random.choice(TECHNICIANS)

        issue = random.choice(ISSUES)

        repair_action = random.choice(ISSUE_ACTIONS[issue])

        follow_up = random.choice(FOLLOW_UP_ACTIONS)

        technician_note = create_technician_note(
            equipment_name=equipment_name,
            issue=issue,
            repair_action=repair_action,
            follow_up=follow_up,
        )

        report_date = (
            (START_DATE + timedelta(days=random.randint(0, 364))).date().isoformat()
        )

        report = {
            "report_id": report_id,
            "report_date": report_date,
            "technician_id": technician_id,
            "technician_name": technician_name,
            "equipment_id": equipment_id,
            "equipment_name": equipment_name,
            "equipment_type": equipment_type,
            "maintenance_category": random.choice(CATEGORIES),
            "issue_type": issue,
            "priority": random.choice(PRIORITIES),
            "location": random.choice(LOCATIONS),
            "downtime_hours": round(
                random.uniform(0.5, 12.0),
                1,
            ),
            "repair_cost": round(
                random.uniform(100.0, 5000.0),
                2,
            ),
            "technician_notes": technician_note,
            "source_system": SOURCE_SYSTEM,
            "source_dataset": SOURCE_DATASET,
            "source_record_id": report_id,
            "is_synthetic": True,
            "is_augmented": False,
            "licence": DATA_LICENCE,
            "ingestion_timestamp": (INGESTION_TIMESTAMP),
            "schema_version": SCHEMA_VERSION,
        }

        reports.append(report)

    return pd.DataFrame(reports)


def save_dataset(
    dataframe: pd.DataFrame,
    output_path: Path = OUTPUT_PATH,
) -> None:
    """Save the generated dataset."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe.to_csv(
        output_path,
        index=False,
    )


def main() -> None:
    """Generate and save the synthetic fixture."""

    dataframe = generate_maintenance_reports()

    save_dataset(dataframe)

    print(dataframe.head())
    print()
    print(f"Rows: {len(dataframe)}")
    print(f"Columns: {len(dataframe.columns)}")
    print(f"Dataset saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
