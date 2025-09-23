friends = 6

#Menu value
dishs = 25
appetizers = 12
drinks = 8

#Menu ordered
dishes_ordered = 3
appetizers_ordered = 2
drinks_ordered = 4

cost = (dishs * dishes_ordered) + (appetizers * appetizers_ordered) + (drinks * drinks_ordered)
total_cost = cost * 1.10 + 5

print(total_cost)
bill = int(total_cost // friends)

print(f"Bill for each person is RM{bill}")