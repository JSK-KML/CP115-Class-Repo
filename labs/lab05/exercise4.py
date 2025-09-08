# Step 1: Take item name and price from the user
item_name = input("Enter the item name: ")
price = float(input("Enter the price of one item (RM): "))

# Step 2: Create variables for quantity and tax rate
quantity = 3
tax_rate = 0.06  # 6%

# Step 3: Calculate costs
subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

# Step 4: Display results
print("\nPurchase Summary:")
print(f"Item Name       : {item_name}")
print(f"Price per Item  : RM{price:.2f}")
print(f"Quantity        : {quantity}")
print(f"Subtotal        : RM{subtotal:.2f}")
print(f"Tax (6%)        : RM{tax_amount:.2f}")
print(f"Total Cost      : RM{total_cost:.2f}")