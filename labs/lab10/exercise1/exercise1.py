position = input()
overtime_hours = int(input())
is_weekend = input()

# Define base hourly rates
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

# Calculate overtime pay (1.5x base rate)
overtime_rate = hourly_rate * 1.5
overtime_pay = overtime_hours * overtime_rate

# Add weekend bonus if applicable
if is_weekend.lower() == "yes":
    weekend_bonus = overtime_hours * 6
    overtime_pay += weekend_bonus

# Total pay is same as overtime pay
total_pay = overtime_pay

if (position == "manager"):
    hourly_rate = 35
elif (position == "supervisor"):
    hourly_rate = 25
else:
    hourly_rate = 18

overtime_pay = (hourly_rate * overtime_hours) * 1.5


if (is_weekend == "no"):
     total_pay = overtime_pay
else:
    total_pay = overtime_pay + (overtime_hours * 5)



    

print(hourly_rate)
print(overtime_pay)
print(total_pay)