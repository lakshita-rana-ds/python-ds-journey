# ==============
# DAY 9 - Pandas - Series + Dataframe basics
# DATE - 10 July, 2026
# STATUS - Done
# ==============

import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 40])
print(s)

# Series with custom labels
s2 = pd.Series([85, 90, 78], index = ["Math", "Science", "English"])
print(s2)
print(s2["Math"])

# DataFrame - a full table
data = {
    "Name": ["Aarav", "Priya", "Rohan"], 
    "Age": [20, 21, 19], 
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)

# Exploring the DataFrame
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(2))
print(df.info())
print(df.describe())

# Selecting columns
print(df["Name"])
print(df[["Name", "Marks"]])

# Selecting rows
print(df.iloc[0])
print(df.loc[0])

# Adding a new column
df["Passed"] = df["Marks"] >= 80
print(df)

# Filtering rows
high_scores = df[df["Marks"] > 80]
print(high_scores)

# ================================
# DAY 9 TASK
# ================================

Students = {
    "Name": ["Sherr", "Cheetah", "Dogii", "Billu", "Puppy"],
    "Age": [17, 16, 9, 4, 7],
    "Marks": [90, 88, 67, 76, 98]
}

dframe = pd.DataFrame(Students)
print(dframe)

dframe.info()
print(dframe.describe())

conditions = [
    dframe["Marks"] >= 90,
    dframe["Marks"] >= 75
]
choices = ["A", "B"]

dframe["Grade"] = np.select(conditions, choices, default = "C")
print(dframe)

high_marks = dframe[dframe["Marks"] > 80]
print(high_marks)