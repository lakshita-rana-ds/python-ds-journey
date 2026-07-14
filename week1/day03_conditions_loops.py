# ==============
# DAY 3 - Conditions and Loops
# DATE - 26 May, 2026
# STATUS - Done
# ==============

# --- PART 1: if / elif / else ---
score = 87

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")           # Grade: B
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Logical operators: and, or, not
age = 20
has_id = True
if age >= 18 and has_id:
    print("Access granted")     # Access granted

# Ternary (one-liner) operator
status = "Pass" if score >= 50 else "Fail"
print(status)                   # Pass



# --- PART 2: for loops ---
# loop over a list
skills = ["Python", "SQL", "ML"]
for skill in skills:
    print(f"Learning: {skill}") 

# range(start, stop, step)
for i in range(2, 10, 2):
    print(i)                    # 2, 4, 6, 8

# enumerate() - index + value together (use this)
companies = ["Micorsoft", "Google", "Amazon"]
for idx, company in enumerate(companies, start = 1):
    print(f"{idx}. {company}")      # here instead of start = 1 we can also use {idx + 1} for indexing.

# Loop over dict .items()
profile = {"name": "Lakshita", "cgpa": 9.8}
for key, value in profile.items():
    print(f"{key} → {value}")



# --- PART 3: While loops ---
# countdown
n = 5
while n > 0:
    print(f"T-minus {n}")
    n -= 1
print("Liftoff! 🚀")

# while True + break (common pattern in real apps)
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("Max attempts reached!")
        break



# --- PART 4: break / continue / pass
# break - exit the loop entirely
for num in range(10):
    if num == 5:
        break
    print(num)          # 0, 1, 2, 3, 4

# continue - skip current iteration
for number in range(10):
    if number == 5:
        continue
    print(number)

# print odds only - using continue
for numb in range(15):
    if numb % 2 == 0:
        continue
    print(numb)        # 1, 3, 5, 7, 9, 11, 13

# pass - just a placeholder, do nothing
for i in range(5):
    pass               # ToDo: fill this later 



# --- PART 5: List Comprehensions ---
# Basic
squares = [i**2 for i in range(1,6)]
print(squares)

# With filter
scores = [45, 82, 91, 38, 76]
passed = [s for s in scores if s >= 50]
print(passed)                       

# Transformation + filter together
hot_temps = [t*1.8+32 for t in [22,35,41] if t > 30]
print(hot_temps)            # [95.0, 105.8]

# Dict comprehension (bonus!)
word_len = {w: len(w) for w in ["Python", "Data", "ML"]}
print(word_len)             # {'Python': 6, 'Data': 4, 'ML': 2}


# ------- END --------







