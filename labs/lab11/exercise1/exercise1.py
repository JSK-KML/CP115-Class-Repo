# Ask how many rounds
num_rounds = int(input())

# Start with no score and no rounds processed
final_score = 0
rounds_processed = 0

# Repeat for each round
for i in range(num_rounds):
    # Get the score for this round
    round_score = int(input())
    
    # Check if score is more than 100
    if round_score > 100:
        # Add 20% bonus
        bonus = round_score * 0.2
        round_score = round_score + bonus
    
    # Add this round's score to the total
    final_score = final_score + round_score
    
    # Count the round
    rounds_processed = rounds_processed + 1

# Show the final score (with 1 decimal place)
print(f"{final_score:.1f}")

# Show how many rounds were processed
print(rounds_processed)
