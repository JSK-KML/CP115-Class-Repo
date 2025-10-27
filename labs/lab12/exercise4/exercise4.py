score_input = input()

passing_count = 0
failing_count = 0

while score_input != "end":
    score = int(score_input)
    if score >= 60:
        passing_count = passing_count + 1
        score_input = input()
        
    else:
        failing_count = failing_count + 1
        score_input = input()

total_count = passing_count + failing_count
if total_count > 0:
    pass_rate = ((passing_count) / (passing_count + failing_count)) * 100
else: pass_rate = 0




        


print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")