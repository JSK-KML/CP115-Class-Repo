score = float(input())

# Initialize counters
score_count = 0
total_score = 0.0

# Prime input already done above
while 0 <= score <= 100:
    # Update totals
    score_count += 1
    total_score += score

    # Update input (ask again)
    score = float(input())

# Calculate average safely
if score_count > 0:
    average_score = total_score / score_count
else:
    average_score = 0.0

# Display results
print(score_count)
print(total_score)
print(f"{average_score:.2f}")
