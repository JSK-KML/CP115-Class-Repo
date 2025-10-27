# Step 1: Take three test scores from the user
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

# Step 2: Calculate total and average score
total = score1 + score2 + score3
average = total / 3

# Step 3: Display individual scores, total, and average
print("\nTest Score Summary:")
print(f"Score 1 : {score1}")
print(f"Score 2 : {score2}")
print(f"Score 3 : {score3}")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")