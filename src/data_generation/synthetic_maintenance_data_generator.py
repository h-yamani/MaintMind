import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

technicians = [
    ("TECH001", "John Smith"),
    ("TECH002", "Sarah Wilson"),
    ("TECH003", "Mike Brown"),
    ("TECH004", "David Taylor"),
    ("TECH005", "Emma Johnson")
]

equipment = [
    ("EQ001", "CAT320 Excavator", "Excavator"),
    ("EQ002", "Komatsu D65", "Bulldozer"),
    ("EQ003", "Hitachi ZX200", "Excavator"),
    ("EQ004", "Hydraulic Press A", "Hydraulic System"),
    ("EQ005", "Generator G1", "Generator"),
    ("EQ006", "Forklift F3", "Forklift")
]

categories = [
    "Hydraulic",
    "Diesel",
    "Electrical",
    "Inspection",
    "Fabrication",
    "Preventive Maintenance"
]

issues = [
    "Hydraulic Leak",
    "Bearing Wear",
    "Electrical Fault",
    "Pressure Loss",
    "Overheating",
    "Safety Concern"
]
issue_actions = {
    "Hydraulic Leak": [
        "Replaced the damaged hydraulic hose and tightened the coupling",
        "Replaced the leaking seal and cleaned the affected area",
        "Tightened loose fittings and completed a pressure test",
    ],
    "Bearing Wear": [
        "Replaced the worn bearing and lubricated the assembly",
        "Adjusted the bearing alignment and tested rotation",
        "Removed the damaged bearing and installed a replacement",
    ],
    "Electrical Fault": [
        "Repaired damaged wiring and tested the electrical circuit",
        "Replaced the faulty relay and verified normal operation",
        "Cleaned the electrical connections and secured loose terminals",
    ],
    "Pressure Loss": [
        "Adjusted the pressure regulator and tested system pressure",
        "Replaced the faulty pressure valve",
        "Inspected the system for leaks and restored operating pressure",
    ],
    "Overheating": [
        "Cleaned the cooling system and checked coolant levels",
        "Replaced the damaged cooling fan",
        "Cleared blocked ventilation and tested operating temperature",
    ],
    "Safety Concern": [
        "Secured the unsafe component and completed a safety inspection",
        "Replaced the damaged safety guard",
        "Isolated the equipment and corrected the identified hazard",
    ],
}

follow_up_actions = [
    "Monitor the equipment during the next operating shift",
    "Schedule a follow-up inspection within two weeks",
    "Review the issue during the next preventive maintenance service",
    "No further action is required unless the issue returns",
    "Inspect related components for similar wear",
]
priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

locations = [
    "Auckland",
    "Hamilton",
    "Tauranga",
    "Wellington"
]

reports = []

start_date = datetime(2025, 1, 1)

for i in range(100):

    equipment_id, equip_name, equip_type = random.choice(equipment)
    technician_id, technician_name = random.choice(technicians)
    issue = random.choice(issues)
    repair_action = random.choice(issue_actions[issue])
    follow_up = random.choice(follow_up_actions)

    note_templates = [
        (
        f"Inspection of {equip_name} identified {issue}. "
        f"{repair_action}. {follow_up}."
        ),
        (
        f"Technician attended {equip_name} following a reported "
        f"{issue}. {repair_action}. Equipment was tested before "
        f"returning to service. {follow_up}."
        ),
        (
        f"{issue} was detected during maintenance of {equip_name}. "
        f"{repair_action}. Operational checks were completed "
        f"successfully. {follow_up}."
        ),
    ]

    technician_note = random.choice(note_templates)

    report = {
        "report_id": f"REP{i+1:03d}",
        "report_date": start_date + timedelta(days=random.randint(0, 365)),
        "technician_id": technician_id,
        "technician_name": technician_name,
        "equipment_id": equipment_id,
        "equipment_name": equip_name,
        "equipment_type": equip_type,
        "maintenance_category": random.choice(categories),
        "issue_type":issue,
        "priority": random.choice(priorities),
        "location": random.choice(locations),
        "downtime_hours": round(random.uniform(0.5, 12), 1),
        "repair_cost": round(random.uniform(100, 5000), 2),
        "technician_notes": technician_note,
    }

    reports.append(report)

df = pd.DataFrame(reports)

df.to_csv(
    "data/maintenance_reports.csv",
    index=False
)

print(df.head())
print()
print("Dataset saved to data/maintenance_reports.csv")
