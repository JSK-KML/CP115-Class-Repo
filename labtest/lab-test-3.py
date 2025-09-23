#Programmer:Muhammad Syafie Bin Ruslin
#Problem: Calculate final price after discount based on user's usage bill

#Receive input
bill = int(input("Please enter bill payment:"))

#Determine discount and calculate final bill
if bill <= 50:
    discount = 1
elif bill <= 100:
    discount = 0.95
else:
    discount = 0.80

final_bill = bill * discount

#Print output
print(f"Bill after discount is RM {final_bill}")