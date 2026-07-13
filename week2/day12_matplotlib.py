# ================
# DAY 12 - Matplotlib: Plots + Charts
# DATE - 13 July, 2026
# STATUS - Done
# ================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: Simple line chart
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Step 2: Bar chart
subjects = ["Math", "Science", "English", "History"]
scores = [86, 92, 78, 88]

plt.bar(subjects, scores, color="skyblue")
plt.title("Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.show()

# Step 3: Histogram
data = np.random.randn(1000)

plt.hist(data, bins=30, color="salmon", edgecolor="black")
plt.title("Histogram of random data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Step 4: Scatter plot
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
marks_scored = [30, 40, 50, 55, 65, 70, 85, 90]

plt.scatter(hours_studied, marks_scored, color = "magenta")
plt.title("Hours Studied vs Marks Scored")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.show()

# Step 5: Multiple plots in one figure (subplots)
fig, axes = plt.subplots(1, 2, figsize = (10, 4))

axes[0].plot(x,y)
axes[0].set_title("Line Chart")

axes[1].bar(subjects, scores)
axes[1].set_title("Bar Chart")

plt.tight_layout()
plt.show()

# ================================
# DAY 12 TASK
# ================================

# 1. Bar chart - sales across 5 months
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 9000, 18000, 21000]

plt.bar(months, sales, color="orange")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (Rs)")
plt.show()

# 2. Histogram of 100+ random values
task_data = np.random.randn(500)

plt.hist(task_data, bins=25, color="purple", edgecolor="black")
plt.title("Distribution of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3. Scatter plot - relationship between two variables
experience_years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salary = [30000, 35000, 40000, 48000, 55000, 62000, 70000, 78000, 85000, 95000]

plt.scatter(experience_years, salary, color="teal")
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary (Rs)")
plt.show()

# 4. Combine all 3 into one figure (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].bar(months, sales, color="orange")
axes[0].set_title("Monthly Sales")

axes[1].hist(task_data, bins=25, color="purple", edgecolor="black")
axes[1].set_title("Random Data Distribution")

axes[2].scatter(experience_years, salary, color="teal")
axes[2].set_title("Experience vs Salary")

plt.tight_layout()
plt.show()