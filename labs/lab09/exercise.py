# multiple conditions with elif
marks = 45
total_marks = 100
percentage = (marks / total_marks) * 100

print(f"Student scored: {percentage}%")

if percentage >= 90:
    print("Grade: A - Excellent!")
elif percentage >= 80:
    print("Grade: B - Good!")
elif percentage >= 70:
    print("Grade: C - Satisfactory!")
elif percentage >= 60:
    print("Grade: D - Pass!")
else:
    print("Grade: F - Fail!")






# else positioning - always last
student_grade = 45

if student_grade >= 90:
    print("Excellent performance")
elif student_grade >= 80:
    print("Good performance")
elif student_grade >= 70:
    print("Satisfactory performance") 
elif student_grade >= 60:
    print("Minimum performance")
else:                        # Always positioned last
    print("Below minimum performance")




# BMI classification - use if-elif-else chain
weight = 85  # kg  
height = 1.75  # meters
bmi = weight / (height * height)

print(f"BMI: {bmi:.1f}")

# Only one classification should apply
if bmi >= 30:
    print("BMI Category: Obese")
elif bmi >= 25:
    print("BMI Category: Overweight")  
elif bmi >= 18.5:
    print("BMI Category: Normal weight")
else:
    print("BMI Category: Underweight")




# Correct: Most specific conditions first
score = 95

if score == 100:
    print("Perfect score!")
elif score >= 90:  
    print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("Below B grade")