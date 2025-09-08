# Test addition and subtraction
result1 = 25 + 15
result2 = 100 - 25
print(f"25 + 15 = {result1}")
print(f"100 - 25 = {result2}")# Test multiplication and division
result3 = 8 * 7
result4 = 20 / 4
print(f"8 * 7 = {result3}")
print(f"20 / 4 = {result4}")# Test floor division, modulus, and powers
result5 = 17 // 5
result6 = 17 % 5
result7 = 3 ** 4
print(f"17 // 5 = {result5}")
print(f"17 % 5 = {result6}")
print(f"3 ** 4 = {result7}")# Test division - always returns float
division = 10 / 2
print(f"10 / 2 = {division} (type: {type(division)})")

# Test floor division - returns int when both operands are int
floor_div = 10 // 3
print(f"10 // 3 = {floor_div} (type: {type(floor_div)})")

# Test modulus - returns int when both operands are int
modulus = 17 % 5
print(f"17 % 5 = {modulus} (type: {type(modulus)})")

# Test exponentiation - returns int when both operands are int
power = 2 ** 3
print(f"2 ** 3 = {power} (type: {type(power)})")# Test mixing int and float in different operations
mixed_division = 15.0 / 4        # float / int = float
mixed_floor = 15.0 // 4          # float // int = float
mixed_modulus = 17.0 % 5         # float % int = float
mixed_power = 2.0 ** 3           # float ** int = float

print(f"15.0 / 4 = {mixed_division} (type: {type(mixed_division)})")
print(f"15.0 // 4 = {mixed_floor} (type: {type(mixed_floor)})")
print(f"17.0 % 5 = {mixed_modulus} (type: {type(mixed_modulus)})")
print(f"2.0 ** 3 = {mixed_power} (type: {type(mixed_power)})")# Compare without and with brackets
result1 = 10 + 3 * 2     
result2 = (10 + 3) * 2    
print(f"10 + 3 * 2 = {result1}")
print(f"(10 + 3) * 2 = {result2}")# Complex BODMAS example
expression = 3 + 2 ** 2 * 4 - 6 / 2
print(f"3 + 2 ** 2 * 4 - 6 / 2 = {expression}")

# Let's break it down step by step
step1 = 2 ** 2    
step2 = step1 * 4  
step3 = 6 / 2     
final = 3 + step2 - step3 
print(f"Step 1 (Powers): 2 ** 2 = {step1}")
print(f"Step 2 (Multiply): {step1} * 4 = {step2}")
print(f"Step 3 (Division): 6 / 2 = {step3}")
print(f"Final: 3 + {step2} - {step3} = {final}")# Same numbers, different brackets = different results
without_brackets = 5 + 3 * 2 ** 2
with_brackets = (5 + 3) * 2 ** 2
different_brackets = 5 + (3 * 2) ** 2
print(f"5 + 3 * 2 ** 2 = {without_brackets}")
print(f"(5 + 3) * 2 ** 2 = {with_brackets}")
print(f"5 + (3 * 2) ** 2 = {different_brackets}")# Test assignment operators
score = 100
print(f"Starting score: {score}")

score += 10     # Add 10
print(f"After += 10: {score}")

score -= 5      # Subtract 5
print(f"After -= 5: {score}")

score *= 2      # Multiply by 2
print(f"After *= 2: {score}")

score //= 3     # Floor division by 3
print(f"After //= 3: {score}")

score %= 15     # Modulus by 15
print(f"After %= 15: {score}")

score **= 2     # Square it
print(f"After **= 2: {score}")# Sequential execution example
print("Step 1: Starting program")
x = 10
print(f"Step 2: x is now {x}")
x = x * 2
print(f"Step 3: x is now {x}")
y = x + 5
print(f"Step 4: y is now {y}")
result = x + y
print(f"Step 5: Final result is {result}")# Order matters in sequential programming
name = "Ali"
age = 20
student_id = "2024001"

# Build information step by step
full_info = f"Name: {name}"
full_info = full_info + f", Age: {age}"
full_info = full_info + f", ID: {student_id}"

print(full_info)

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