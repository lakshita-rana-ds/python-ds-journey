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
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

full_example("must", 1, 2, x=10, y=20)



# --- TOPIC 4: lambda ---



