grade = float(input())

# TODO: Your code here
total = 0
valid_count = 0

while grade >= 0:  
    if 0 <= grade <= 100:
        total += grade
        valid_count += 1
    
    grade = float(input())


if valid_count > 0:
    average = total / valid_count
else:
    average = 0.0

print(valid_count)
print(f"{average:.2f}")
