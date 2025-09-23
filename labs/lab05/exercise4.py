name = input("Item name: ")
price = float(input("Item price: "))
quantity = int(input("Quantity: "))
subtotal = price * quantity
taxamount = subtotal * 0.06
totalcost = subtotal + taxamount

print("Subtotal is",subtotal)
print("Tax amount is",taxamount)
print("Total cost is",totalcost)