# TODO: Your code here

found_number = 0

for number in range(1, 101):  
    if number % 7 == 0 and number % 13 == 0:
        found_number = number
        break  

print(found_number)
