price = float(input())


item_count = 0
total_cost = 0.0


while price >= 0:
    
    item_count += 1
    total_cost += price

    price = float(input())

print(item_count)
print(f"{total_cost:.2f}")
