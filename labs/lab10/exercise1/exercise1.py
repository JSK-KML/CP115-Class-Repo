position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here

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