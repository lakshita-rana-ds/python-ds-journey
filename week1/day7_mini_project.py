# week1/day7_mini_project.py
# Day 7: Week 1 Mini Project — Student Grade Calculator
# Uses: variables, data structures, loops, functions,
#       file handling, OOP, list comprehensions, exceptions
# github.com/lakshita-rana-ds/python-ds-journey

import csv

class Student:
    def __init__(self, name, branch, scores):
        self.name = name
        self.branch = branch
        self.scores = scores

    def average(self):
        return round(sum(self.scores) / len(self.scores), 1)

    def grade(self):
        avg = self.average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 55:
            return "C"
        else:
            return "F"

    def status(self):
        return "Pass" if self.average() >= 55 else "Fail"

    def __str__(self):
        return (f"{self.name} ({self.branch}) | "
                f"Avg: {self.average()} | Grade: {self.grade()} | {self.status()}")


def create_sample_csv(filename):
    """Create a sample CSV if none exists."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "branch", "scores"])
        writer.writerows([
            ["Lakshita", "CSE DS", "88;92;79;95;84"],
            ["Riya",     "CSE DS", "55;61;48;72;59"],
            ["Arjun",    "CSE DS", "90;85;91;88;94"],
            ["Priya",    "CSE DS", "35;42;50;38;45"],
        ])


def load_students(filename):
    """Load students from CSV file."""
    students = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                scores = [int(x) for x in row["scores"].split(";")]
                students.append(Student(row["name"], row["branch"], scores))
    except FileNotFoundError:
        print(f"Creating {filename} with sample data...")
        create_sample_csv(filename)
        return load_students(filename)
    return students


def print_report(students):
    """Print full class report."""
    print("\n" + "=" * 55)
    print("  WEEK 1 CAPSTONE: STUDENT GRADE CALCULATOR")
    print("=" * 55)

    for s in students:
        print(f"  {s}")

    avgs = [s.average() for s in students]
    class_avg = round(sum(avgs) / len(avgs), 1)
    top = max(students, key=lambda s: s.average())
    passed = [s.name for s in students if s.status() == "Pass"]

    print(f"\n  Class average : {class_avg}")
    print(f"  Top student   : {top.name} ({top.average()})")
    print(f"  Passed ({len(passed)})    : {', '.join(passed)}")
    print("=" * 55)


# --- Run ---
students = load_students("students_data.csv")
print_report(students)