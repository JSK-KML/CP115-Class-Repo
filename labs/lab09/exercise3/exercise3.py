day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# Determine base price using separate if statements (no nesting)
base_price = 0

# Weekend Adult pricing
if day_type == "Weekend" and customer_type == "Adult":
    base_price = 18

# Weekend Child pricing  
if day_type == "Weekend" and customer_type == "Child":
    base_price = 12

# Weekend Senior pricing
if day_type == "Weekend" and customer_type == "Senior":
    base_price = 15

# Weekday Adult pricing
if day_type == "Weekday" and customer_type == "Adult":
    base_price = 15

# Weekday Child pricing
if day_type == "Weekday" and customer_type == "Child":
    base_price = 10

# Weekday Senior pricing
if day_type == "Weekday" and customer_type == "Senior":
    base_price = 12

# Start with base price as final price
final_price = base_price

# Apply evening surcharge (after 6pm = show_time > 18)
if show_time > 18:
    final_price = final_price + 3

# Apply student discount (10% off final price, weekdays only)
if day_type == "Weekday" and is_student == "Yes":
    final_price = final_price * 0.9

print(base_price)
print(final_price)