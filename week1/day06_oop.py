# ==============
# DAY 6 - OOP: Classes, Objects, Inheritance
# DATE - 5 June, 2026
# STATUS - Done
# ==============

# --- TOPIC 1: class and __init__ — the blueprint ---
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
s1 = Student("Lakshita", 9.2)
s2 = Student("Riya", 7.8)
print(s1.name)      # Lakshita
print(s2.cgpa)      # 7.8



# --- TOPIC 2: self - what  it actually means ---
class Student: 
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
s1 = Student("Lakshita", 9.2)
s2 = Student("Riya", 7.8)
print(s1.name, s2.name)         # Lakshita Riya
s1.cgpa = 9.5 
print(s1.cgpa, s2.cgpa)         # 9.5 7.8



# --- TOPIC 3: methods — giving objects behavior ---
class Student: 
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        """Calculate average score."""
        return sum(self.scores) / len(self.scores)

    def get_grade(self):
        avg = self.average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"

    def __str__(self):
        """Defines what print(object) shows."""
        return f"{self.name}: {self.average():.1f} ({self.get_grade()})"


# Example usage:
s1 = Student("Lakshita", [88, 92, 79])
print(s1.average())     # 86.33333333333333
print(s1)               # Lakshita: 86.3 (A) - uses __str__



# --- TOPIC 4: Inheritance - reusing and extending classes ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

# Student INHERITS from Person class
class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)     # calls Person's __init__
        self.branch = branch

    def introduce(self):
        base = super().introduce()      # reuse parent's method
        return f"{base}, studying {self.branch}"

# Creating an instance and testing
s = Student("Lakshita", 19, "CSE DS")
print(s.introduce())
# Output: Hi, I'm Lakshita, 19 years old, studying CSE DS



# --- TOPIC 5: real world example - BankAccount ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdraw {amount}. New balance: {self.balance}")

# Execution Flow Example:
account = BankAccount("Lakshita", 5000)
account.deposit(2000)   # Deposited 2000. New balance: 7000
account.withdraw(1000)  # Withdrew 1000. New balance: 6000
account.withdraw(99999) # Insufficient funds
    







