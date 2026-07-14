# ================
# DAY 15 - Statistics: Mean, Median, Mode, Variance, Std Dev
# DATE - 14 July, 2026
# STATUS - Done
# ================

import numpy as np
import pandas as pd
import statistics as stats

marks = [78, 85, 92, 65, 88, 92, 74]

# Step 1: Mean
mean_value = np.mean(marks)
print("Mean:", mean_value)

# Step 2: Median
median_value = np.median(marks)
print("Median:", median_value)

scores = [70, 85, 70, 90, 85, 70, 60]

# Step 3: Mode
mode_value = stats.mode(scores)
print("Mode:", mode_value)

# Step 4: Variance
variance_value = np.var(marks)
print("Variance:", variance_value)

# Step 5: Standard Deviation
std_value = np.std(marks)
print("Standard Deviation:", std_value)

# Step 6: Same stats using a DataFrame
df = pd.DataFrame({
    "Student": ["Aarav", "Priya", "Rohan", "Meera", "Kabir"],
    "Marks": [78, 85, 92, 65, 88]
})

print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].var())
print(df["Marks"].std())
print(df.describe())

# ================================
# DAY 15 TASK
# ================================

# Using NumPy/statistics
cars_sold = [890, 360, 670, 950, 700, 294, 770, 830]

cars_mean = np.mean(cars_sold)
print("Mean value of cars sold:", cars_mean)

cars_median = np.median(cars_sold)
print("Median value of cars sold:", cars_median)

cars_mode = stats.mode(cars_sold)
print("Mode value of cars sold:", cars_mode)

cars_var = np.var(cars_sold)
print("Variation of cars sold:", cars_var)

cars_std = np.std(cars_sold)
print("Standard Deviation of cars sold:", cars_std)

# Using pandas method
dframe = pd.DataFrame({
    "Brand": ["Hyundai", "Honda", "Mercedes", "Tata", "Audi", "Land Rover", "Toyota", "Maruti Suzuki"],
    "Cars Sold": [890, 360, 670, 950, 700, 294, 770, 830]
})

print("Mean (cars sold):", dframe["Cars Sold"].mean())
print("Median (cars sold):", dframe["Cars Sold"].median())
print("Mode (cars sold):", dframe["Cars Sold"].mode())
print("Variation (cars sold):", dframe["Cars Sold"].var())
print("Standard Deviation (cars sold):", dframe["Cars Sold"].std())
print(dframe.describe())

# INTERPRETATION
# The standard deviation (~239) is quite large relative to the mean (683),
# meaning cars sold varies significantly across brands - some brands sell
# as few as 294 units while others sell nearly 950, rather than being
# clustered tightly around the average. Also note: since every value in
# this dataset is unique (no repeats), there's no meaningful mode here -
# pandas returns all values as tied, while statistics.mode() arbitrarily
# picks the first one it sees.