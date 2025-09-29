# Ask for age and number of accidents
age = int(input("Enter your age: "))
accidents = int(input("Enter number of accidents: "))

# Step 1: Base premium by age
if age < 25:
    premium = 2400
elif age <= 50:
    premium = 1800
else:
    premium = 2000

# Step 2: Accident penalty
if accidents == 0:
    premium = premium  # no change
elif accidents <= 2:
    premium = premium + 300
else:
    premium = premium + 600

# Step 3: Good driver discount
if accidents == 0:
    discount = premium * 0.10
    premium = premium - discount

# Show final result
print("Your insurance premium is RM", premium)
