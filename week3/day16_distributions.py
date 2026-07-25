# ================
# DAY 16 - Statistics - Distributions (Normal, Binomial, Poisson)
# DATE - 24 July, 2026
# STATUS - Done
# ================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Step 1: Normal Distribution
normal_data = np.random.normal(loc=50, scale=10, size=1000)

sns.histplot(normal_data, bins=30, kde=True, color="skyblue")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.show()

print("Mean:", np.mean(normal_data))
print("Std Dev:", np.std(normal_data))

# 68-95-99.7 rule check
mean = np.mean(normal_data)
std = np.std(normal_data)

within_1_std = ((normal_data > mean - std) & (normal_data < mean + std)).mean()
print("Percentage within 1 std dev:", within_1_std * 100)

# Step 2: Binomial Distribution
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)

sns.histplot(binomial_data, bins=11, color="salmon")
plt.title("Binomial Distribution (10 coin flips, 1000 times)")
plt.xlabel("Number of Successes")
plt.show()

# Step 3: Poisson Distribution
poisson_data = np.random.poisson(lam=4, size=1000)

sns.histplot(poisson_data, bins=15, color="seagreen")
plt.title("Poisson Distribution (avg 4 events)")
plt.xlabel("Number of Events")
plt.show()

# Step 4: All 3 side by side
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.histplot(normal_data, bins=30, kde=True, ax=axes[0], color="skyblue")
axes[0].set_title("Normal")

sns.histplot(binomial_data, bins=11, ax=axes[1], color="salmon")
axes[1].set_title("Binomial")

sns.histplot(poisson_data, bins=15, ax=axes[2], color="seagreen")
axes[2].set_title("Poisson")

plt.tight_layout()
plt.show()

# ================================
# DAY 16 TASK
# ================================

# 1. Normal distribution - own mean/std, verify 1 std dev percentage
task_normal = np.random.normal(loc=70, scale=15, size=1000)

task_mean = np.mean(task_normal)
task_std = np.std(task_normal)

task_within_1_std = ((task_normal > task_mean - task_std) & (task_normal < task_mean + task_std)).mean()

print("\nTask Normal - Mean:", task_mean)
print("Task Normal - Std Dev:", task_std)
print("Task Normal - Percentage within 1 std dev:", task_within_1_std * 100)

sns.histplot(task_normal, bins=30, kde=True, color="skyblue")
plt.title("Task: Normal Distribution (mean=70, std=15)")
plt.xlabel("Value")
plt.show()

# 2. Binomial - 20 trials, 30% success probability, 500 repetitions
task_binomial = np.random.binomial(n=20, p=0.3, size=500)

sns.histplot(task_binomial, bins=15, color="salmon")
plt.title("Task: Binomial Distribution (20 trials, p=0.3, 500 times)")
plt.xlabel("Number of Successes")
plt.show()

# 3. Poisson - own average rate
task_poisson = np.random.poisson(lam=7, size=1000)

sns.histplot(task_poisson, bins=15, color="seagreen")
plt.title("Task: Poisson Distribution (avg 7 events)")
plt.xlabel("Number of Events")
plt.show()

# 4. Combine all 3 into one figure
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.histplot(task_normal, bins=30, kde=True, ax=axes[0], color="skyblue")
axes[0].set_title("Task Normal (mean=70, std=15)")

sns.histplot(task_binomial, bins=15, ax=axes[1], color="salmon")
axes[1].set_title("Task Binomial (n=20, p=0.3)")

sns.histplot(task_poisson, bins=15, ax=axes[2], color="seagreen")
axes[2].set_title("Task Poisson (lam=7)")

plt.tight_layout()
plt.show()