#Score from each test
score1 = 78
score2 = 85
score3 = 92
score4 = 67
score5 = 88

#Total score and average score
total_score = score1 + score2 + score3 + score4 + score5
average_score = total_score / 5

#How many each test contribute to total score
cscore1 = score1 / total_score * 100
cscore2 = score2 / total_score * 100
cscore3 = score3 / total_score * 100
cscore4 = score4 / total_score * 100
cscore5 = score5 / total_score * 100

#Print
print(f"Each test score is : \n Test 1 = {score1} \n Test 2 = {score2} \n Test 3 = {score3} \n Test 4 = {score4} \n Test 5 = {score5}")
print(f"Total score is {total_score}")
print(f"Student average is {average_score}")
print(f"Each test contribute: \n Test 1 = {cscore1}% \n Test 2 = {cscore2}% \n Test 3 = {cscore3}% \n Test 4 = {cscore4}% \n Test 5 = {cscore5}%")