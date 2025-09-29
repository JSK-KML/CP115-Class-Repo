# Ask for the target points
target = int(input())

# Start with 0 points and 0 rounds
total = 0
rounds = 0

# Keep asking until total reaches or passes the target
while total < target:
    points = int(input())
    total = total + points   # add points to total
    rounds = rounds + 1      # count this round

# Show results after loop ends
print(total)
print(rounds)

