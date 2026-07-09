# ==============
# DAY 8 - NumPy - Arrays + Operations
# DATE - 9 July, 2026
# STATUS - Done
# ==============

import numpy as np

# Step 1: Create a basic 1D array
a = np.array([1, 2, 3, 4])
print("1D array:", a)                    # 1D array: [1 2 3 4]

# Step 2: Create a 2D array (matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", b)
# 2D array:
#  [[1 2 3]
#  [4 5 6]]

# Step 3: Check shape, dimensions, and data type
print("Shape of a:", a.shape)             # Shape of a: (4,)
print("Shape of b:", b.shape)             # Shape of b: (2, 3)
print("Dimensions of b:", b.ndim)         # Dimensions of b: 2
print("Data type of a:", a.dtype)         # Data type of a: int64

# Step 4: Quick array creation methods
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones(5)
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("Zeros:\n", zeros_arr)
# Zeros:
#  [[0. 0. 0.]
#  [0. 0. 0.]]

print("Ones:", ones_arr)                  # Ones: [1. 1. 1. 1. 1.]
print("Arange:", range_arr)               # Arange: [0 2 4 6 8]
print("Linspace:", linspace_arr)          # Linspace: [0.   0.25 0.5  0.75 1.  ]

# Step 5: Indexing and slicing
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])           # First element: 10
print("Last element:", arr[-1])           # Last element: 50
print("Slice [1:4]:", arr[1:4])           # Slice [1:4]: [20 30 40]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("matrix[0,2]:", matrix[0, 2])       # matrix[0,2]: 3
print("Row 1:", matrix[1, :])             # Row 1: [4 5 6]
print("Column 0:", matrix[:, 0])          # Column 0: [1 4]

# Step 6: Vectorized operations
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
print("Addition:", x + y)                 # Addition: [11 22 33]
print("Subtraction:", x - y)              # Subtraction: [-9 -18 -27]
print("Multiplication:", x * y)           # Multiplication: [10 40 90]
print("Division:", y / x)                 # Division: [10. 10. 10.]
print("Square:", x ** 2)                  # Square: [1 4 9]

# Step 7: Boolean masking
sample = np.array([4, 9, 1, 7, 3])
print("Greater than 5 mask:", sample > 5)
# Greater than 5 mask: [False  True False  True False]

print("Filtered values:", sample[sample > 5])
# Filtered values: [9 7]

# Step 8: Summary functions
print("Sum:", sample.sum())               # Sum: 24
print("Mean:", sample.mean())             # Mean: 4.8
print("Max:", sample.max())               # Max: 9
print("Min:", sample.min())               # Min: 1
print("Std Dev:", sample.std())           # Std Dev: 2.85...
sample.sort()
print("Sorted:", sample)                  # Sorted: [1 3 4 7 9]

# ================================
# DAY 8 TASK
# ================================

# 1. Create a 5x5 array of random integers between 1 and 100
task_arr = np.random.randint(1, 100, size=(5, 5))
print("\nTask array:\n", task_arr)
# Task array:
#  [[73 12 88 45  6]     <- RANDOM, will be different every run
#  [34 91  5 67 23]
#  [56 12 78  9 44]
#  [ 3 65 87 21 55]
#  [90 14 33 76  8]]

# 2. Print shape, mean, max, min
print("Shape:", task_arr.shape)           # Shape: (5, 5)
print("Mean:", task_arr.mean())           # Mean: ~46.5 (varies)
print("Max:", task_arr.max())             # Max: ~91 (varies)
print("Min:", task_arr.min())             # Min: ~3 (varies)

# 3. Replace all values greater than 50 with 0
task_arr[task_arr > 50] = 0
print("Modified array (values > 50 replaced with 0):\n", task_arr)
# Modified array:
#  [[ 0 12  0 45  6]     <- values that were >50 are now 0
#  [34  0  5  0 23]
#  [ 0 12  0  9 44]
#  [ 3  0  0 21  0]
#  [ 0 14 33  0  8]]