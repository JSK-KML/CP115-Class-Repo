age = int(input())
accident_count = int(input())

# Your code here
if age < 25:
    base_premium = 2400
    if accident_count == 0:
        penalty=0
        total_premium = base_premium + penalty 
    elif accident_count < 3:
        penalty=300
        total_premium = base_premium + penalty 
    else:
        penalty=600
        total_premium = base_premium + penalty 
elif age >= 25 and age <= 50:
    base_premium = 1800
    if accident_count == 0:
        penalty=0
        total_premium = base_premium + penalty 
    elif accident_count < 3:
        penalty=300
        total_premium = base_premium + penalty 
    else:
        penalty=600
        total_premium = base_premium + penalty 
else:
    base_premium=2000
    if accident_count == 0:
        penalty=0
        total_premium = base_premium + penalty 
    elif accident_count < 3:
        penalty=300
        total_premium = base_premium + penalty 
    else:
        penalty=600
        total_premium = base_premium + penalty 

if accident_count == 0:
    discount_amount = 0.90
else:
    discount_amount = 1

final_premium = total_premium * discount_amount

print(base_premium)
print(final_premium)
print(discount_amount)