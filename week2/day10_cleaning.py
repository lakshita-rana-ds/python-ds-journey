# ================
# DAY 10 - Pandas - Data Cleaning
# DATE - 11 July, 2026
# STATUS - Done
# ================

import pandas as pd
import numpy as np

# Step 1: Create messy data on purpose (to practice cleaning it)
data = {
    "Name": ["Aarav", "Priya", None, "Rohan", "Priya"],
    "Age": [20, 21, 19, np.nan, 21],
    "Marks": [85, 92, 78, 60, 92]
}

df = pd.DataFrame(data)
print(df)

# Step 2: Detecting missing values
print(df.isnull())
print(df.isnull().sum())

# Step 3: Handling missing values

# Option A - drop rows with any missing value
df_dropped = df.dropna()
print(df_dropped)

# Option B - fill missing values instead of dropping
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Name"] = df_filled["Name"].fillna("Unknown")
print(df_filled)

# Step 4: Detecting and removing duplicates
print(df.duplicated())
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)

# Step 5: Checking and fixing data types
print(df.dtypes)
df["Age"] = df["Age"].astype("Int64")
print(df.dtypes)

# ================================
# DAY 10 TASK
# ================================

# 1. Print how many missing values exist in each column
print("\nMissing values per column:")
print(df.isnull().sum())

# 2. Fill missing Age with column mean, missing Name with "Unknown"
df_task = df.copy()
df_task["Age"] = df_task["Age"].astype("Float64")   # allow decimals again
df_task["Age"] = df_task["Age"].fillna(df_task["Age"].mean())
df_task["Name"] = df_task["Name"].fillna("Unknown")

# 3. Remove duplicate rows
df_task = df_task.drop_duplicates()

# 4. Print the final cleaned DataFrame
print("\nFinal cleaned DataFrame:")
print(df_task)
