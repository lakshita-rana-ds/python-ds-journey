# ================
# DAY 11 - Pandas - GroupBy + Merge + Filtering
# DATE - 12 July, 2026
# STATUS - Done
# ================

import pandas as pd
import numpy as np

# Step 1: GroupBy basics
data = {
    "Student": ["Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha"],
    "Subject": ["Math", "Math", "Science", "Science", "Math", "Science"],
    "Marks": [85, 92, 78, 88, 95, 70]
}

df = pd.DataFrame(data)
print(df)

# Group by Subject and get average marks per subject
grouped = df.groupby("Subject")["Marks"].mean()
print(grouped)

# Other agregations
print(df.groupby("Subject")["Marks"].sum())
print(df.groupby("Subject")["Marks"].count())
print(df.groupby("Subject")["Marks"].max())

# Multiple stats at once
print(df.groupby("Subject")["Marks"].agg(["mean", "max", "min", "count"]))

# Step 2: Merge basics 
students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Aarav", "Priya", "Rohan", "Meera"]
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Marks": [85, 92, 78, 88]
})

merged = pd.merge(students, marks, on="StudentID")
print(merged)

# Merge with mismatched IDs - inner vs left
students2 = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Aarav", "Priya", "Rohan"]
})

marks2 = pd.DataFrame({
    "StudentID": [1, 2, 4],
    "Marks": [85, 92, 60]
})

inner = pd.merge(students2, marks2, on="StudentID", how="inner")
left = pd.merge(students2, marks2, on="StudentID", how="left")

print(inner)
print(left)

# Step 3: Filtering with multiple conditions
high_math = df[(df["Subject"] == "Math") & (df["Marks"] > 90)]
print(high_math)

math_or_high = df[(df["Subject"] == "Math") | (df["Marks"] > 90)]
print(math_or_high)

# ================================
# DAY 11 TASK
# ================================

# 1. Create a DataFrame of at least 6 employees: Name, Department, Salary
employees = pd.DataFrame({
    "Name": ["Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha"],
    "Department": ["Engineering", "Engineering", "Sales", "Sales", "Engineering", "Marketing"],
    "Salary": [75000, 82000, 60000, 65000, 90000, 55000]
})
print("\nEmployees:")
print(employees)

# 2. Average salary per department
avg_salary_dept = employees.groupby("Department")["Salary"].mean()
print("\nAverage salary per department:")
print(avg_salary_dept)

# 3. Merge with a Department -> Manager mapping
managers = pd.DataFrame({
    "Department": ["Engineering", "Sales", "Marketing"],
    "Manager": ["Nikhil", "Sana", "Devansh"]
})

employees_with_managers = pd.merge(employees, managers, on="Department")
print("\nEmployees with managers:")
print(employees_with_managers)

# 4. Filter: earning above overall average salary AND in a specific department
overall_avg = employees["Salary"].mean()
top_engineering = employees_with_managers[
    (employees_with_managers["Salary"] > overall_avg) &
    (employees_with_managers["Department"] == "Engineering")
]
print("\nTop earners in Engineering (above overall average):")
print(top_engineering)