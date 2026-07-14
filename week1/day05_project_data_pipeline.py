# ======================================

# ---------- DAY 5 - PROJECT -----------

# STUDENT DATA PIPELINE
# DATE - 3 June, 2026

# ======================================


import csv

def save_students_csv(students, filename):
    """Save student data to a CSV file."""
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Scores", "Average", "Grade"])
            for name, scores in students.items():
                avg = round(sum(scores) / len(scores), 1)
                grade = "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 55 else "F"
                writer.writerow([name, scores, avg, grade])
        print(f"Saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def load_and_analyse(filename):
    """Load CSV and print analysis."""
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        print(f"\nLoaded {len(rows)} students from {filename}")
        print("-" * 40)

        averages = []
        for row in rows:
            print(f"{row['Name']:10} | Avg: {row['Average']:5} | Grade: {row['Grade']}")
            averages.append(float(row["Average"]))

        overall = round(sum(averages) / len(averages), 1)
        top = max(rows, key=lambda r: float(r["Average"]))
        print(f"\nClass average : {overall}")
        print(f"Top student   : {top['Name']} ({top['Average']})")

    except FileNotFoundError:
        print(f"Error: {filename} not found. Run save first.")
    except Exception as e:
        print(f"Unexpected error: {e}")

students = {
    "Lakshita": [88, 92, 79, 95, 84],
    "Riya":     [55, 61, 48, 72, 59],
    "Arjun":    [90, 85, 91, 88, 94],
    "Priya":    [35, 42, 50, 38, 45],
}

save_students_csv(students, "students.csv")
load_and_analyse("students.csv")
load_and_analyse("missing.csv")  # tests FileNotFoundError