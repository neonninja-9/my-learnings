"""
Fixed & Optimized Synthetic Attendance Data Generator

Generates an attendance CSV with:
 - missing values
 - duplicate rows
 - wrong date formats
 - inconsistent attendance entries
 - malformed employee IDs
 - random errors (bad dates, typos, NaN, etc.)

Output: synthetic_attendance_raw.csv
"""

import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

RNG = np.random.default_rng(12345)
random.seed(12345)

OUTFILE = "synthetic_attendance_raw.csv"
NUM_EMPLOYEES = 30
DAYS = 90   # change to 365 if needed
START_DATE = datetime(2024, 1, 1)

# Canonical attendance types
ATT_CANONICAL = ["Present", "Absent", "Late", "Holiday", "Sick"]

# Inconsistent variants
ATT_VARIANTS = {
    "Present": ["P", "present", "Present ", "p", "1", "Y", "On Duty", "on-duty"],
    "Absent":  ["A", "absent", "Absent ", "0", "N", "Not Present"],
    "Late":    ["L", "late", "Late ", "Tardy"],
    "Holiday": ["H", "holiday", "Holiday ", "hol", "OFF"],
    "Sick":    ["S", "sick", "Sick ", "SL"]
}

# --------------------- Helper Functions --------------------------

def random_date_str(base_date, idx):
    """Return random date formats (including invalid ones)."""
    dt = base_date + timedelta(days=idx)
    formats = [
        dt.strftime("%Y-%m-%d"),
        dt.strftime("%d-%m-%Y"),
        dt.strftime("%d/%m/%Y"),
        dt.strftime("%m/%d/%Y"),
        dt.strftime("%Y.%m.%d"),
        dt.strftime("%d %b %Y"),
        dt.strftime("%Y/%m/%d"),
        "2024-02-30" if RNG.random() < 0.05 else dt.strftime("%d-%b-%Y")
    ]
    return random.choice(formats)


# --------------------- Generate Base Records ---------------------

employees = []
for i in range(1, NUM_EMPLOYEES + 1):
    emp_id = f"E{i:03d}"

    # introduce some inconsistent ID formatting
    if i % 7 == 0:
        emp_id = emp_id.lower()
    if i % 11 == 0:
        emp_id = " " + emp_id

    employees.append({"EmployeeID": emp_id, "Name": f"Employee_{i:03d}"})


rows = []

for day_index in range(DAYS):
    for emp in employees:

        true_att = RNG.choice(ATT_CANONICAL, p=[0.7, 0.15, 0.08, 0.03, 0.04])
        att_variant = RNG.choice(ATT_VARIANTS[true_att])

        # Work hours
        if true_att in ["Present", "Late"]:
            hours = round(max(0, RNG.normal(8, 1)), 2)

            start_hour = 9 + RNG.normal(0, 0.5)
            end_hour = start_hour + hours

            check_in = f"{int(start_hour):02d}:{int((start_hour%1)*60):02d}"
            check_out = f"{int(end_hour):02d}:{int((end_hour%1)*60):02d}"
        else:
            hours = np.nan
            check_in = np.nan
            check_out = np.nan

        rows.append({
            "Date": random_date_str(START_DATE, day_index),
            "EmployeeID": emp["EmployeeID"],
            "Name": emp["Name"],
            "Attendance": att_variant,
            "HoursWorked": hours,
            "CheckIn": check_in,
            "CheckOut": check_out
        })

df = pd.DataFrame(rows)

# --------------------- Inject Problems ---------------------------

# 1) Missing values
for col in ["Attendance", "HoursWorked", "Name"]:
    mask = RNG.random(len(df)) < 0.02
    df.loc[mask, col] = np.nan

# 2) Exact duplicates
duplicates = df.sample(frac=0.02, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# 3) Near-duplicates (same emp+date)
near_dups = df.sample(frac=0.02, random_state=99)
near_rows = []

for _, row in near_dups.iterrows():
    new_row = row.copy()

    # Change attendance randomly
    new_row["Attendance"] = RNG.choice(["P", "Present", "A", "Absent", "Late"])

    # Change hours slightly
    if not pd.isna(new_row["HoursWorked"]):
        new_row["HoursWorked"] = round(max(0, new_row["HoursWorked"] + RNG.normal(0, 1)), 2)

    near_rows.append(new_row)

df = pd.concat([df, pd.DataFrame(near_rows)], ignore_index=True)

# 4) Messy Employee IDs
for i in df.sample(frac=0.03, random_state=13).index:
    val = df.at[i, "EmployeeID"]
    df.at[i, "EmployeeID"] = f" {str(val).strip().lower()} "

# 5) Completely invalid dates
bad_dates = df.sample(frac=0.01, random_state=21).index
for i in bad_dates:
    df.at[i, "Date"] = random.choice([
        "32/13/2024", "not_a_date", "2024-99-99", "Feb 30 2024"
    ])

# 6) Corrupt names safely
for i in df.sample(frac=0.02, random_state=7).index:
    val = df.at[i, "Name"]
    if isinstance(val, str):
        df.at[i, "Name"] = val.replace("_", " ").upper()

# 7) Shuffle final rows
df = df.sample(frac=1, random_state=1).reset_index(drop=True)

# Save file
df.to_csv(OUTFILE, index=False)
print(f"Synthetic attendance dataset generated: {OUTFILE}")
print("Total rows:", len(df))
