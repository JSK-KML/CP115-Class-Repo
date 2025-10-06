# exercise2.py - Circle Calculator
import math

# Get radius input from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")