#Define
base_membership = 120
personal_training = 80
locker_rental = 25
towel_service = 15
otr_fee = 50

#Calculation
first_month = base_membership + personal_training * 6 + locker_rental + towel_service
other_month = 11 * (base_membership + personal_training * 6 + locker_rental + towel_service)
annual_cost = first_month + other_month

print(f"Total annual cost is RM{annual_cost}")

