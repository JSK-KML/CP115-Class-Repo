monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Determine max loan amount (5x income)
max_loan_amount = monthly_income * 5

# Determine interest rate based on credit score
if credit_score >= 700:
    interest_rate = 3.5
elif credit_score >= 600:
    interest_rate = 5.5
else:
    interest_rate = 0.0

# Check approval criteria
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
else:
    approval_status = "Rejected"
    interest_rate = 0.0  # No interest for rejected loans

print(interest_rate)
print(max_loan_amount)
print(approval_status)