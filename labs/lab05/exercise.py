# Lab 05 Exercise File
# This file serves as a placeholder for lab05 exercises
# Examples of valid identifiers and variables
student_name = "Alice"
age = 20
total_score = 95.5
is_enrolled = True
course_code = "CP115"

# Examples of identifier naming conventions
firstName = "John"        # camelCase (less common in Python)
first_name = "Jane"       # snake_case (Python convention)
MAXIMUM_ATTEMPTS = 3      # UPPER_CASE for constants
# Let's see Python keywords
import keyword
print(keyword.kwlist)
# Numeric data types
age = 21                    # int (integer)
height = 5.9               # float (floating-point number)
temperature = -15.5        # float (can be negative)

# String data type
student_name = "Muhammad Ali"    # str (string)
course_title = 'Python Programming'  # str (single or double quotes)
description = """This is a multi-line
string that spans several lines."""   # str (triple quotes)

# Boolean data type
is_active = True           # bool (boolean)
has_submitted = False      # bool (boolean).

# Special data type
nothing = None             # NoneType (represents absence of value)
## Try this
print(type(age))
print(type(temperature))
print(type(student_name))
print(type(is_active))
print(type(nothing))
# Import entire modules
import math
import random
import datetime

# Using imported modules
circle_area = math.pi * (5 ** 2)
random_number = random.randint(1, 100)
current_date = datetime.date.today()

# Import specific functions from modules
from math import sqrt, pow, sin, cos
from random import choice, shuffle
from datetime import datetime, timedelta

# Using imported functions directly (no module prefix needed)
square_root = sqrt(25)
power_result = pow(2, 8)
random_choice = choice(['apple', 'banana', 'cherry'])
# Basic input and output
print("Welcome to the Grade Calculator!")
print("This program will calculate your course grade.")

# Getting user input (always returns a string)
student_name = input("Enter your name: ")
course_name = input("Enter the course name: ")

# Getting numeric input requires conversion
assignment_score = float(input("Enter your assignment score (0-100): "))
exam_score = float(input("Enter your exam score (0-100): "))
participation_score = float(input("Enter your participation score (0-100): "))

# Calculating final grade
final_grade = (assignment_score * 0.4) + (exam_score * 0.5) + (participation_score * 0.1)

# Formatted output using string concatenation
print()
print("Student: " + student_name)
print("Course: " + course_name)
print("Final Grade: " + str(final_grade) + "%")