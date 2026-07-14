# ==============
# DAY 5 - File Handling and Exception Handling
# DATE - 28 May, 2026
# STATUS - Done
# ==============

# --- TOPIC 1: reading files — open() and read() ---
with open("data.txt", "w") as f:
    f.write("Line 1: Hello\nLine 2: Python\nLine 3: Data Science\n")
# Three ways to read a file
with open("data.txt", "r") as f:
    content = f.read() 
# entire file as one string 
print(content) 
with open("data.txt", "r") as f: 
    lines = f.readlines() 
# list of lines 
print(lines) 
with open("data.txt", "r") as f: 
    for line in f: 
# line by line (most memory efficient) 
        print(line.strip()) # strip() removes \n



# --- TOPIC 2: writing files - write modes ---
# "w" - write (creates file, overwrites if exists)
with open("output.txt", "w") as f:
    f.write("Hello, Lakshita!\n")
    f.write("Day 5 of Python DS Journey\n")
# "a" - append (adds to end, doesn't overwrite) 
with open("output.txt", "a") as f:
    f.write("Adding one more line\n")
# "r" - read only (default)
# "w" - write (overwrites!)
# "a" - append
# "r+" = read and write



# --- TOPIC 3: try/except/finally - handle errors gracefully ---
# Basic try/except
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError: 
    print("Cannot divide by zero!")

# finally - always runs, even if error occurs
try:
    with open("data.txt", "r") as f:
        data = f.read() 
except FileNotFoundError:
    print("File not found! Check the path.")
    data = ""
finally:
    print("Done - this always runs")
# catch any exception (use sparingly)
try:
    risky_code()
except Exception as e: 
    print(f"Error: {e}")



# --- TOPIC 4: common exceptions to know ---
# FileNotFoundError - file doesn't exist
except FileNotFoundError:
    print("File not found")
# ValueError - wrong type of value
except ValueError:
    print("Invalid value")
# ZeroDivisionError - dividing by zero
except ZeroDivisionError:
    print("Cannot divide by zero")
# IndexError - list index out of range
except IndexError:
    print("Index out of range")
# KeyError - dict key doesnt exist
except KeyError:
    print("Key not found in dict")
# TypeError - wrong data type
except TypeError:
    print("Wrong data type")



# --- CSV files - the DS bread and butter ---
import csv
# Writing a csv file
students = [["Name", "Score", "Grade"], ["Lakshita", 87.6, "A"], ["Riya", 59.0, "C"], ["Arjun", 89.6, "A"],]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
# Reading a CSV file
with open("Students.csv", "r") as f:
    reader = csv.DictReader(f)
# reads as dict - best way
    for row in reader:
        print(f"{row['Name']}: {row['Score']}")