# ==============
# DAY 1 - Variables, Data Types, Type Casting, f-strings
# DATE - 24 May, 2026
# STATUS - Done
# ==============

# --- PART 1: Variables ---
name = "Lakshita"
age = 18
cgpa = 8.2
is_student = True

print(name)          # Lakshita
print(age)           # 18      
print(cgpa)          # 8.2
print(is_student)    # True   

x, y, z = 10, 20, 30
print(x, y, z)   # 10 20 30



# --- PART 2: Data Types ---
""" students = 45
negative = -123
print(type(students))     # <class 'int'>

marks = 95.4
pi = 3.1415
print(type(marks))     # <class 'float'>

college = "Bennett University"
city = "Greater Noida"
print(type(city))     # <class 'str'> 

passed = True
failed = False
print(type(passed))     # <class 'bool'> """



# --- PART 3: Type Casting ---
""" # String to int
age_str = "19"
age_int = int(age_str)
print(age_int + 1)     # 20

# String to float
price_str = "299.99"
price_float = float(price_str)
print(price_float)     # 299.99

# int to string
roll = 2010
roll_str = str(roll)
print("Roll number: " + roll_str)     # Roll number: 2010

# float to int
gpa = 8.8
gpa_int = int(gpa)
print(gpa_int)     # 8

# int to float
marks = 87
marks_float = float(marks)
print(marks_float)     # 87.0

# String to bool
print(bool("Hello"))        # True
print(bool(43))             # True
print(bool(0))              # False
print(bool(85.9))           # True
print(bool(""))             # False """



# --- PART 4: Strings in Depth ---
""" name = "Abcd University"

# Length
print(len(name))                    # 15

# Uppercase / Lowercase
print(name.upper())                 # ABCD UNIVERSITY
print(name.lower())                 # abcd university

# Check if something is inside the string
print("Abcd" in name)               # True
print("Delhi" in name)              # False

# Replace
print(name.replace("Abcd", "Delhi"))  # Delhi University
 
# Split
code = "Python Java C++ SQL"
languages = code.split()
print(languages)                    # ['Python', 'Java', 'C++', 'SQL']

fruit = "Apple, Mango, Banana"
result = fruit.split(",")
print(result)                       # ['Apple', 'Mango', 'Banana']

vegetable = "Potato Tomato Ginger"
print(vegetable.split())            # ['Potato', 'Tomato', 'Ginger']

# Split - maxsplit
text = "one two three four"
print(text.split(" ", 2))       # limits how many splits happen # ['one', 'two', 'three four']

# Strip
messy = "  Hello World    "
print(messy.strip())            # Hello World

# Indexing
word = "Python"
print(word[0])                  # P
print(word[-2])                 # o

# Slicing
print(word[0:3])                # Pyt
print(word[:2])                 # Py
print(word[3:])                 # hon """



# --- PART 5: f-strings ---
""" name = "Lakshita"
age = 18
cgpa = 8.6
branch = "CSE Data Science"

# Old way
print("My name is " + name + " and I am " + str(age) + " years old.")   # My name is Lakshita and I am 18 years old.

# f-string way      (no need to type cast)
print(f"My name is {name} and I am {age} years old.")       # My name is Lakshita and I am 18 years old.
print(f"Branch: {branch} | Cgpa: {cgpa}")                   # Branch: CSE Data Science | Cgpa: 8.6

marks = 456
total = 500
print(f"Marks: {marks}/{total}")                            # 456/500
print(f"Percentage: {marks/total * 100:.2f}") # :.2f means show only 2 decimal places   # 91.20


price = 1499.4567
print(f"Price: {price:.2f}")
print(f"Price: {price:.0f}")
print(f"Rounded: {round(price)}")

name = "abcd"
print(f"{name :>15}")  #               abcd (right alligned 15 spaces) """



# --- PART 6: Basic Operators ---
""" a = 11
b = 5

print(a + b)    # 16  — addition
print(a - b)    # 6  — subtraction
print(a * b)    # 55  — multiplication
print(a / b)    # 2.2 — division (always float)
print(a // b)   # 2   — floor division (removes decimal)
print(a % b)    # 1   — modulus (remainder)
print(a ** b)   # 161051 — power (11 to the power 5)

# Comparison Operators
print(10 > 5)    # True
print(10 == 10)  # True  (== is comparison, = is assignment)
print(10 != 5)   # True  (!= is not equals to)
print(3 >= 3)    # True """



# ---PRACTICE PROBLEMS---
# Problem 1 — Basic variables:Create variables for your name, age, college, and CGPA. Print them all in one f-string line like: "Name: Aryan | Age: 19 | College: Bennett | CGPA: 8.5"

# Solution 1
""" name = "Lakshita"
age = 18
college = "Bennett University"
cgpa = 8.8
print(f"Name: {name} | Age: {age} | College: {college} | CGPA: {cgpa}") """


# Problem 2 — Type casting: Ask the user to enter their maths and science marks using input(). Convert them to integers. Print their total and average using an f-string. Format average to 2 decimal places.

# Solution 2
""" marks_math = input("Enter marks scored in maths: ")
marks_sci= input("Enter marks scored in science: ")
marks_maths = int(marks_math)
marks_science = int(marks_sci)
print(f"Total marks: {marks_maths + marks_science}")
print(f"Average marks: {(marks_maths + marks_science)/2:.2f}") """



#Problem 3 — String operations:
  # Take the string "  data science with python  ". Write code to:
    # Remove extra spaces
    # Capitalise the first letter of each word
    # Count how many times the letter "a" appears
    # Replace "python" with "Python"
    # Print the length of the cleaned string

# Solution 3
""" subject = "  data science with python  "
cleaned_str = subject.strip()
print("Removed extra spaces: " + cleaned_str)
print("Capitalised first letter of each word: " + cleaned_str.title()) # title (capitalize is used for only first word)
print("Count of 'a': " + str(cleaned_str.count('a'))) # for lowercase count(subject.lower().count() same for upper.)
print("Replaced 'python' with 'Python': " + cleaned_str.replace("python", "Python"))
print("Length of cleaned string: " + str(len(cleaned_str))) """



# Problem 4 — Type detection: Create 5 variables of different types. Write a program that prints the value AND the type of each variable in this format: "Value: 8.5 | Type: <class 'float'>"

# Solution 4
""" var_float = 5.23
var_int = 7
var_str = "Hello"
var_bool = True
var_list = [10, 20, 30]
print(f"Value: {var_float} | Type: {type(var_float)}")
print(f"Value: {var_int} | Type: {type(var_int)}")
print(f"Value: {var_str} | Type: {type(var_str)}")
print(f"Value: {var_bool} | Type: {type(var_bool)}")
print(f"Value: {var_list} | Type: {type(var_list)}") """


# Problem 5 — Real DS scenario: You have a dataset row as strings: age = "23", salary = "45000.50", is_employed = "True". Convert each to their correct data type. Then print: "Age: 23 | Salary: ₹45000.50 | Employed: True"

# Solution 5
""" age = "23"
salary = "45000.50"
is_employed = "True"
age_int = int(age)
salary_float = float(salary)
is_employed_bool = is_employed == "True"
print(f"Age: {age_int} | Salary: {salary_float:.2f} | Employed: {is_employed_bool}") """


