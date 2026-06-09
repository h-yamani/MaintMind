import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

technicians = [
    "John Smith",
    "Sarah Wilson",
    "Mike Brown",
    "David Taylor",
    "Emma Johnson"
]

equipment = [
    ("CAT320 Excavator", "Excavator"),
    ("Komatsu D65", "Bulldozer"),
    ("Hitachi ZX200", "Excavator"),
    ("Hydraulic Press A", "Hydraulic System"),
    ("Generator G1", "Generator"),
    ("Forklift F3", "Forklift")
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

    equip_name, equip_type = random.choice(equipment)

    report = {
        "report_id": f"REP{i+1:03d}",
        "report_date": start_date + timedelta(days=random.randint(0, 365)),
        "technician_name": random.choice(technicians),
        "equipment_name": equip_name,
        "equipment_type": equip_type,
        "maintenance_category": random.choice(categories),
        "issue_type": random.choice(issues),
        "priority": random.choice(priorities),
        "location": random.choice(locations),
        "downtime_hours": round(random.uniform(0.5, 12), 1),
        "repair_cost": round(random.uniform(100, 5000), 2),
        "technician_notes":
            f"Performed maintenance on {equip_name}. "
            f"Detected {random.choice(issues)} and completed repair. "
            f"Recommend follow-up inspection."
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
