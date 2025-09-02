"""

# Test addition and subtraction
result1 = 25 + 15
result2 = 100 - 25
print(f"25 + 15 = {result1}")
print(f"100 - 25 = {result2}")

# Test multiplication and division
result3 = 8 * 7
result4 = 20 / 4
print(f"8 * 7 = {result3}")
print(f"20 / 4 = {result4}")

# Test floor division, modulus, and powers
result5 = 17 // 5
result6 = 17 % 5
result7 = 3 ** 4
print(f"17 // 5 = {result5}")
print(f"17 % 5 = {result6}")
print(f"3 ** 4 = {result7}") """

"""
# Test division - always returns float
division = 10 / 2
print(f"10 / 2 = {division} (type: {type(division)})")

# Test floor division - returns int when both operands are int
floor_div = 10.5 // 3
print(f"10 // 3 = {floor_div} (type: {type(floor_div)})")

# Test modulus - returns int when both operands are int
modulus = 17 % 5
print(f"17 % 5 = {modulus} (type: {type(modulus)})")

# Test exponentiation - returns int when both operands are int
power = 2 ** 3
print(f"2 ** 3 = {power} (type: {type(power)})")"""

"""
# Same numbers, different brackets = different results
without_brackets = 5 + 3 * 2 ** 2
with_brackets = (5 + 3) * 2 ** 2
different_brackets = 5 + (3 * 2) ** 2
print(f"5 + 3 * 2 ** 2 = {without_brackets}")
print(f"(5 + 3) * 2 ** 2 = {with_brackets}")
print(f"5 + (3 * 2) ** 2 = {different_brackets}")"""

"""
# Sequential execution example
print("Step 1: Starting program")
x = 10
print(f"Step 2: x is now {x}")
x = x * 2
print(f"Step 3: x is now {x}")
y = x + 5
print(f"Step 4: y is now {y}")
result = x + y
print(f"Step 5: Final result is {result}")
"""
"""
# Order matters in sequential programming
name = "Ali"
age = 20
student_id = "2024001"

# Build information step by step
full_info = f"Name: {name}"
full_info = full_info + f", Age: {age}"
full_info = full_info + f", ID: {student_id}"

print(full_info)"""

# This code proves sequential execution
print("Line 1: This will run")
print("Line 2: This will also run") 
x = 10
print(f"Line 3: x = {x}")
y = x * 2
print(f"Line 4: y = {y}")
print("Line 5: All good so far")

# This line has an intentional error
print(unknown_variable)  # This will cause an error