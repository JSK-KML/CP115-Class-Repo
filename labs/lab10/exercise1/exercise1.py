position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
hourly_rate=1.5

if position == "Manager" and is_weekend == "Yes":
    overtime_pay = overtime_hours * 35 * 1.5
    total_pay = overtime_pay + (overtime_hours * 5)
elif position == "Manager" and is_weekend == "No":
    overtime_pay = overtime_hours * 35 * 1.5
    total_pay = overtime_pay
elif position == "Supervisor" and is_weekend == "Yes":
    overtime_pay = overtime_hours * 25 * 1.5
    total_pay = overtime_pay + (overtime_hours * 5)
elif position == "Supervisor" and is_weekend == "No":
    overtime_pay = overtime_hours * 25 * 1.5
    total_pay = overtime_pay
elif position == "Staff" and is_weekend == "Yes":
    overtime_pay = overtime_hours * 18 * 1.5
    total_pay = overtime_pay + (overtime_hours * 5)
else:
    overtime_pay = overtime_hours * 18 *1.5
    total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)