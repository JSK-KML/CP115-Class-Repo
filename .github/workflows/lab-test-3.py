# Name: Muhammad Syahdiq Asyraf Bin Tipilil @ Rapahil
# Write a set of code that can receive monthly usage from customers,discount received or not and calculate total bill

# Ask user to insert monthly usage 

usage = float(input("Enter monthly usage:"))

# Determining the discount that customer will get and the total bill they received

if (usage < 50):
    total_bill = usage
elif (usage < 101):
    total_bill = usage - (usage * 0.05)
else:
    total_bill = usage - (usage *0.2)

# Output of the coding

print(total_bill)



