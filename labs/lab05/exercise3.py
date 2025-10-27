import random

# Step 2: Take the student's class name from the user
class_name = input("Enter your class name: ")

# Step 3: Generate a random number
random_number = random.randint(1, 100)  # You can change the range if needed

# Display class information
print("\nClass Information:")
print(f"Class Name: {class_name}")
print(f"Generated Class ID: {random_number}")