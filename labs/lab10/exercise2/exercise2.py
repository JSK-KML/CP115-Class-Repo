age = int(input())
accident_count = int(input())

# Determine base premium
if age < 25:
    base_premium = 2400
elif age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

# Calculate penalties or discounts
if accident_count == 0:
    discount_amount = int(base_premium * 0.10)
    final_premium = base_premium - discount_amount
else:
    penalty = accident_count * 300
    if penalty > 600:
        penalty = 600
    final_premium = base_premium + penalty
    discount_amount = 0

print(base_premium)
print(final_premium)
print(discount_amount)
