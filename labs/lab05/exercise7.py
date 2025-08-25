# Step 1: Import the math module
import math

# Step 2: Take one number from the user
number = float(input("Enter a number: "))

# Step 3: Perform calculations
square_root = math.sqrt(number)
square = math.pow(number, 2)
cube = math.pow(number, 3)
sine = math.sin(math.radians(number))  # Convert to radians for math.sin

# Step 4: Display the results
print("\nMath Operations Result:")
print(f"Square root of {number} : {square_root}")
print(f"Square of {number}      : {square}")
print(f"Cube of {number}        : {cube}")
print(f"Sine of {number}°       : {sine}")  