score1 = 85
score2 = 92.5
score3 = 78

#Calculate
average= score1 + score2 + score3
print(f"Average score is {average} (type is: {type(average)})")

int_average = int(average)
print(f"Average score is {int_average} (type is: {type(int_average)})")

calculate = score1**2/score2 + score3 % 7
print(f"Calculation for score is {calculate} (type is: {type(calculate)})")

#Convert and print
print(int(score2))
print(float(score1))