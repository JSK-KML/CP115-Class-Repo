# Ask how many days we will monitor
num_days = int(input())

# Ask the warning threshold temperature
threshold = float(input())

# Start counters
total_temp = 0        # total of all temperatures
danger_days = 0       # count of days above threshold

# Repeat for each day
for i in range(1, num_days + 1):
    # Get temperature for the day
    temp = float(input())
    
    # Add to total (for average later)
    total_temp = total_temp + temp
    
    # Check if above threshold
    if temp > threshold:
        danger_days = danger_days + 1

# Calculate average temperature
average = total_temp / num_days

# Show results
print(danger_days)
print(average)
