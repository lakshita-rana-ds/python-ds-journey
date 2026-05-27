# ==============
# DAY 2 - Lists, Tuples, Sets, Dictionaries with Indexing, Slicing, nested structures and methods.
# DATE - 25 May, 2026
# STATUS - Done
# ==============

# ---PART 1: Lists
students = ["Lakshita", "Aryan", "Priya", "Rohit"]
marks = [78, 83, 91, 69]
mixed = ["Hello", 3, True, 5.89]

print(students)             # ['Lakshita', 'Aryan', 'Priya', 'Rohit']
print(marks)                # [78, 83, 91, 69]
print(mixed)                # ['Hello', 3, True, 5.89]
print(type(students))       # <class 'list'>

# List- Indexing
fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits[0])        # apple
print(fruits[3])        # orange
print(fruits[4])        # grapes
print(fruits[-1])       # grapes
print(fruits[-5])       # apple

# List- Slicing
fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits[1:3])    # ['banana', 'mango']
print(fruits[0:3])    # ['apple', 'banana', 'mango']
print(fruits[:3])     # ['apple', 'banana', 'mango']
print(fruits[2:])     # ['mango', 'orange', 'grapes']
print(fruits[:])      # entire list
print(fruits[::2])    # ['apple', 'mango', 'grapes']  — every 2nd item [start:end:step]
print(fruits[::-1])   # ['grapes', 'orange', 'mango', 'banana', 'apple'] — reversed

# List- Methods
marks = [85, 92, 78, 95, 88]
marks.append(76)          # adds at end → [85, 92, 78, 95, 88, 76]
marks.insert(0, 100)      # adds at position 0 → [100, 85, 92, 78, 95, 88, 76]
marks.remove(78)          # removes first occurrence of 78
popped = marks.pop()      # removes and returns last item --output- 76
popped2 = marks.pop(0)    # removes and returns item at index 0 --output- 100
print(len(marks))         # 4
print(max(marks))         # 95
print(min(marks))         # 85
print(sum(marks))         # 360
print(marks.count(85))    # 1
print(marks.index(92))    # 1
marks.sort()              # ascending [85, 88, 92, 95]
marks.sort(reverse=True)  # descending [95, 92, 88, 85]
print(sorted(marks))      # ascending — does NOT change original list [85, 88, 92, 95]
marks.reverse()           # reverses in place

# List- Nested Lists
students = [
    ["Lakshita", 92, "CSE"],
    ["Aryan", 85, "CSE"],
    ["Priya", 78, "ECE"]
]

print(students[0])         # ['Lakshita', 92, 'CSE']
print(students[0][0])      # Lakshita
print(students[1][1])      # 85
print(students[2][2])      # ECE



# --- PART 2: Tuples ---
""" coordinates = (28.6139, 77.2090)
rgb = (255, 128, 0)
person = ("Lakshita", 19, "Bennett")

print(coordinates)       # (28.6139, 77.209)
print(type(coordinates)) # <class 'tuple'>
print(person[0])         # Lakshita
print(person[-1])        # Bennett
print(person[0:2])       # ('Lakshita', 19)

# Tuple- Unpacking
person = ("Lakshita", 19, "Bennett")
name, age, college = person
print(name)      # Lakshita
print(age)       # 19
print(college)   # Bennett

# Swap two variables using tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)      # 20 10
 """


# --- PART 3: Sets ---
""" numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "mango", "apple", "banana"}

print(numbers)    # {1, 2, 3, 4, 5}
print(fruits)     # {'mango', 'apple', 'banana'} — duplicates removed automatically
print(type(fruits)) # <class 'set'>

# Sets- Operations
python_students = {"Lakshita", "Aryan", "Priya", "Rohit"}
sql_students = {"Aryan", "Rohit", "Sneha", "Raj"}

print(python_students | sql_students)   # {'Lakshita', 'Aryan', 'Priya', 'Rohit', 'Sneha', 'Raj'} -Union
print(python_students & sql_students)   # {'Aryan', 'Rohit'}   -Intersection
print(python_students - sql_students)   # {'Lakshita', 'Priya'}
print("Aryan" in python_students)       # True
print("Sneha" in python_students)       # False

# Sets- Methods
skills = {"Python", "SQL", "Excel"}

skills.add("Tableau")         # add one item
skills.update(["ML", "DS"])   # add multiple items
skills.remove("Excel")        # remove item (gives error if not found)
skills.discard("Java")        # remove item (no error if not found)
print(len(skills))            # 5

# Sets- Removing duplicates from a set
cities = ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Chennai"]
unique_cities = list(set(cities))
print(unique_cities)   # ['Chennai', 'Bangalore', 'Delhi', 'Mumbai']
 """


# --- PART 4: Dictionary ---
""" student = {
    "name": "Lakshita",
    "age": 19,
    "college": "Bennett University",
    "cgpa": 8.5,
    "branch": "CSE Data Science"
}

print(student)
print(type(student))   # <class 'dict'>

student = {"name": "Lakshita", "age": 19, "cgpa": 8.5}

# Method 1 — direct (gives error if key doesn't exist)
print(student["name"])          # Lakshita
print(student["cgpa"])          # 8.5
# Method 2 — .get() (returns None if key doesn't exist)
print(student.get("age"))       # 19
print(student.get("marks"))     # None
print(student.get("marks", 0))  # 0    -default value if not found

# Dictionary- Modify
student = {"name": "Lakshita", "age": 19, "cgpa": 8.5}
student["branch"] = "CSE Data Science"
student["cgpa"] = 9.0
del student["age"]
print("name" in student)        # True
print("marks" in student)       # False
print(student)                  # {'name': 'Lakshita', 'cgpa': 9.0, 'branch': 'CSE Data Science'}

# Dictionary- Methods
student = {
    "name": "Lakshita",
    "age": 19,
    "cgpa": 8.5,
    "branch": "CSE DS"
}

print(student.keys())    # dict_keys(['name', 'age', 'cgpa', 'branch'])
print(student.values())  # dict_values(['Lakshita', 19, 8.5, 'CSE DS'])
print(student.items())   # dict_items([('name','Lakshita'), ('age',19)...])
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Lakshita
# age: 19
# cgpa: 8.5
# branch: CSE DS

# Dictionary- Nested
dataset = {
    "Student1": {"name": "Lakshita", "marks": "92", "grade": "A"},
    "Student2": {"name": "Aryan", "marks": "86", "grade": "B"},
    "Student3": {"name": "Priya", "marks": "80", "grade": "B"}
}

print(dataset["Student1"]["name"])      # Lakshita
print(dataset["Student2"]["marks"])     # 86

for student_id, info in dataset.items():
    print(f"{student_id}: {info['name']} scored {info['marks']}")
# Output:
# Student1: Lakshita scored 92
# Student2: Aryan scored 86
# Student3: Priya scored 80
 """


# --- PRACTICE PROBLEMS ---
# Problem 1 — List operations: Create a list of 5 subject names. Add 2 more subjects. Remove the 3rd subject. Sort alphabetically. Print the final list and its length.

# Solution 1
subjects = ["Hindi", "English", "Maths", "Science", "Economics"]
subjects += ["History", "Geography"]        # Extend method can also be used or 2 times append
subjects.pop(2)
subjects.sort()
print(subjects)
print(f"Total sujects: {len(subjects)}")

# Problem 2 — List slicing: Create a list of numbers 1 to 10. Using slicing print: first 5 numbers, last 3 numbers, every alternate number, the list in reverse.

# Solution 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"First 5 numbers: {my_list[:5]}")
print(f"Last 3 numbers: {my_list[7:]}")
print(f"Every alternate number: {my_list[::2]}")
print(f"List in reverse: {my_list[::-1]}")


# Problem 3 — Tuple unpacking: Create a tuple with your name, age, college, branch and CGPA. Unpack it into 5 separate variables. Print each in a formatted f-string.

# Solution 3
my_info = ("Lakshita", 18, "Bennett University", "Data Science CSE", 8.4)
name, age, college, branch, cgpa = my_info
print(f"""
--- Student Profile ---
Name    : {name}
Age     : {age}
College : {college}
Branch  : {branch}
Cgpa    : {cgpa:.2f}
""")


# Problem 4 — Set real use case:
# You have two lists:
# pythonmorning_batch = ["Lakshita", "Aryan", "Priya", "Rohit", "Sneha"]
# evening_batch = ["Aryan", "Rohit", "Raj", "Meera", "Priya"]
# Using sets find: students in both batches, students only in morning, all unique students across both batches.

# Solution 4
morning_batch = ["Lakshita", "Aryan", "Priya", "Rohit", "Sneha"]
evening_batch = ["Aryan", "Rohit", "Raj", "Meera", "Priya"]
morning_set = set(morning_batch)
evening_set = set(evening_batch)
print(f"Students in both batches: {morning_set & evening_set}")
print(f"Students only in morning: {morning_set - evening_set}")
print(f"All unique students across both batches: {morning_set | evening_set}")


# Problem 5 — Dictionary DS scenario: Create a dictionary for 3 of your subjects with their marks. Add a 4th subject. Update one mark. Calculate and print the average marks using f-string formatted to 2 decimal places. Loop through and print each subject and mark.

# Solution 5
my_dict = {"History": 98, "Maths": 92, "Science": 96}
my_dict["English"] = (97)
my_dict["Maths"] = (95)
print(f"{sum(my_dict.values())/len(my_dict.values()):.2f}")
for subject, mark in my_dict.items():
    print(f"{subject}: {mark}")






