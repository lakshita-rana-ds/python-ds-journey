# ======================================

# ---------- DAY 4 - PROJECT -----------

# STUDENT REPORT CARD GENERATOR
# DATE - 3 June, 2026

# ======================================



def calculate_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

def get_grade(avg):
    """Convert average score to letter grade."""
    if avg >= 85: return "A"
    elif avg >= 70: return "B"
    elif avg >= 55: return "C"
    else: return "F"

def generate_report(name, scores, passing=55):
    """
    Generate a report card for one student.

    Args:
        name (str): Student name.
        scores (list): List of numeric scores.
        passing (float): Minimum average to pass. Default 55.

    Returns:
        dict: Report with avg, grade, status, high, low.
    """
    avg = calculate_average(scores)
    return {
        "name":   name,
        "avg":    round(avg, 1),
        "grade":  get_grade(avg),
        "status": "Pass" if avg >= passing else "Fail",
        "high":   max(scores),
        "low":    min(scores),
    }

def print_report(report):
    """Print a formatted report card."""
    print(f"\n{report['name']}")
    print(f"  Avg   : {report['avg']}")
    print(f"  Grade : {report['grade']}")
    print(f"  Status: {report['status']}")
    print(f"  High  : {report['high']} | Low: {report['low']}")

students = {
    "Lakshita": [88, 92, 79, 95, 84],
    "Riya":     [55, 61, 48, 72, 59],
    "Arjun":    [90, 85, 91, 88, 94],
    "Priya":    [35, 42, 50, 38, 45],
}

print("=" * 40)
print("  REPORT CARD GENERATOR")
print("=" * 40)

reports = [generate_report(n, s) for n, s in students.items()]
for r in reports:
    print_report(r)

# Sort by avg using lambda
top = sorted(reports, key=lambda r: r["avg"], reverse=True)
print(f"\nTop student: {top[0]['name']} ({top[0]['avg']})")



# --------------- END -----------------

