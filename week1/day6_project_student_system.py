# week1/day6_project_student_system.py
# Day 6 Project: Student Management System (OOP)
# github.com/lakshita-rana-ds/python-ds-journey

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class Student(Person):
    def __init__(self, name, age, branch, scores):
        super().__init__(name, age)
        self.branch = branch
        self.scores = scores

    def average(self):
        return round(sum(self.scores) / len(self.scores), 1)

    def grade(self):
        avg = self.average()
        if avg >= 85: return "A"
        elif avg >= 70: return "B"
        elif avg >= 55: return "C"
        else: return "F"

    def status(self):
        return "Pass" if self.average() >= 55 else "Fail"

    def report(self):
        return (f"{self.name} ({self.branch})\n"
                f"  Avg: {self.average()} | Grade: {self.grade()} | {self.status()}")

    def __str__(self):
        return self.report()


students = [
    Student("Lakshita", 19, "CSE DS", [88, 92, 79, 95, 84]),
    Student("Riya",     19, "CSE DS", [55, 61, 48, 72, 59]),
    Student("Arjun",    20, "CSE DS", [90, 85, 91, 88, 94]),
    Student("Priya",    19, "CSE DS", [35, 42, 50, 38, 45]),
]

print("=" * 40)
print("  STUDENT MANAGEMENT SYSTEM")
print("=" * 40)

for s in students:
    print()
    print(s)

top = max(students, key=lambda s: s.average())
print(f"\nTop student: {top.name} ({top.average()})")