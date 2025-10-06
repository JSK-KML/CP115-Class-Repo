position = input()
overtime_hours = int(input())
is_weekend = input()

# Set base hourly rate
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 0

# Base overtime pay (1.5x)
overtime_pay = overtime_hours * (hourly_rate * 1.5)

# Weekend bonus (extra RM6/hour)
if is_weekend == "Yes":
    overtime_pay = overtime_pay + (overtime_hours * 6)

# Total pay = same as overtime_pay
total_pay = overtime_pay

print(hourly_rate)
print(int(overtime_pay))
print(int(total_pay))
