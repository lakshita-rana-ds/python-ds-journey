# ================
# DAY 13 - Seaborn: Statistical Visualisation
# DATE - 13 July, 2026
# STATUS - Done
# ================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: Sample Dataset
data = {
    "Department": ["Engineering", "Engineering", "Sales", "Sales", "Marketing", "Marketing", "Engineering", "Sales"],
    "Salary": [75000, 82000, 60000, 65000, 55000, 58000, 90000, 62000],
    "Experience": [2, 4, 1, 3, 2, 5, 6, 2]
}

df = pd.DataFrame(data)
print(df)

# Step 2: Sample dataset
sns.barplot(data=df, x="Department", y="Salary")
plt.title("Average Salary by Department")
plt.show()

# Step 3: Box plot
sns.boxplot(data=df, x="Department", y="Salary")
plt.title("Salary Distribution by Department")
plt.show()

# Step 4: Histogram with separate KDE curve
random_data = np.random.randn(1000)

sns.histplot(random_data, bins=30, color="skyblue", stat="density")
sns.kdeplot(random_data, color="darkblue", linewidth=2)
plt.title("Distribution with KDE")
plt.show()

# Step 5: Scatter plot with hue
sns.scatterplot(data=df, x="Experience", y="Salary", hue="Department", s=100)
plt.title("Experience vs Salary by Department")
plt.show()

# Step 6: Heatmap = correlation between numeric columns
numeric_df = df[["Salary", "Experience"]]
correlation = numeric_df.corr()
print(correlation)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ================================
# DAY 13 TASK
# ================================

# Own dataset: at least 8 rows, 1 categorical + 2 numeric columns
task_data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Bangalore", "Delhi", "Mumbai"],
    "Rent": [25000, 35000, 22000, 28000, 40000, 30000, 27000, 38000],
    "CommuteTime": [45, 60, 40, 35, 65, 30, 50, 55]
}

task_df = pd.DataFrame(task_data)
print(task_df)

# 1. Bar plot - average Rent by City
sns.barplot(data=task_df, x="City", y="Rent")
plt.title("Average Rent by City")
plt.show()

# 2. Box plot - Rent spread/outliers by City
sns.boxplot(data=task_df, x="City", y="Rent")
plt.title("Rent Distribution by City")
plt.show()

# 3. Scatter plot with hue
sns.scatterplot(data=task_df, x="CommuteTime", y="Rent", hue="City", s=100)
plt.title("Commute Time vs Rent by City")
plt.show()

# 4. Correlation heatmap
task_numeric = task_df[["Rent", "CommuteTime"]]
task_correlation = task_numeric.corr()
print(task_correlation)

sns.heatmap(task_correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap - Rent vs Commute Time")
plt.show()


