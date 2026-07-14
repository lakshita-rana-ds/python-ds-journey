# ==============
# DAY 4 - Functions
# DATE - 27 May, 2026
# STATUS - Done
# ==============

# --- TOPIC 1: def and return ---
# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Lakshita"))

# Multiple return values (returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([1, 3, 5, 7, 9])
print(low, high)            # 1 9



# --- TOPIC 2: Default Arguments ---
def format_salary(amount, currency="INR"):
    return f"{currency} {amount}"

print(format_salary(27000000))      # INR 27000000
print(format_salary(85000, "USD"))  # USD 85000
# Always put default argument AFTER non-default one. def f(a=1, b) is a SyntaxError.



# --- TOPIC 3: *args and **kwargs ---
# *args (collects into tuples)
def total_score(*scores):
    return sum(scores)

print(total_score(89, 92, 89, 97))      # 367
print(total_score(67, 86, 79, 90, 91))  #413

# **kwargs
def student_profile(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

student_profile(name="Lakshita", cgpa=9.2, branch="CSE DS")

# combining all three - order must be: required, *args, **kwargs
def full_example(required, *args, **kwargs):
    print(f"required: {required}")  # required: must
    print(f"args: {args}")          # args: (1, 2)
    print(f"kwargs: {kwargs}")      # kwargs: {'x': 10, 'y': 20}

full_example("must", 1, 2, x=10, y=20)



# --- TOPIC 4: lambda ---
# Regular vs lambda
def square(x): return x**2
square_l = lambda x: x**2

print(square(5))    # 25
print(square_l(5))  # 25

# Real use: sort a list of dicts by a key
students = [
    {"name": "Riya",     "cgpa": 7.8},
    {"name": "Lakshita", "cgpa": 9.2},
    {"name": "Arjun",    "cgpa": 8.9},
]

ranked = sorted(students, key=lambda s: s["cgpa"], reverse=True)
for s in ranked:
    print(f"{s['name']}: {s['cgpa']}")
# Lakshita: 9.2 | Arjun: 8.9 | Riya: 7.8

# map() + lambda
scores = [45, 82, 91, 38]
boosted = list(map(lambda s: s * 1.1, scores))
# [49.5, 90.2, 100.1, 41.8]



# --- TOPIC 5: Scope (local vs global)
x = 10  # global

def show_scope():
    x = 99  # local — does NOT touch the global x
    print(f"inside: {x}")   # 99

show_scope()
print(f"outside: {x}")      # 10 — unchanged!

# global keyword — use very rarely
def update_global():
    global x
    x = 999

update_global()
print(x)  # 999



# --- TOPIC 6: Docstrings ---
def calculate_grade(score):
    """
    Convert a numeric score to a letter grade.

    Args:
        score (float): Score between 0 and 100.

    Returns:
        str: Letter grade A, B, C, or F.
    """
    if score >= 85: return "A"
    elif score >= 70: return "B"
    elif score >= 55: return "C"
    else: return "F"



# ------- END --------





