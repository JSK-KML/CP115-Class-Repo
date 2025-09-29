# Step 1: Take time in minutes from the user
total_minutes = int(input("Enter time in minutes: "))

# Step 2: Convert minutes to hours and remaining minutes
hours = total_minutes // 60
minutes = total_minutes % 60

# Step 3: Display original minutes and converted time
print("\nTime Conversion Result:")
print(f"Original Time: {total_minutes} minutes")
print(f"Converted Time: {hours} hour(s) and {minutes} minute(s)")