employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
total_salary = base_salary + (overtime_hours*35)
if tax_status == Single and total_salary >= 5000:
    tax_rate = 22%
    net_salary = total_salary * 1.22
else:
    tax_rate = 18%
    net_salary = total_salary * 1.18
if tax_status == Married and total_salary >= 6000:
    tax_rate = 20%
    net_salary = total_salary * 1.20
else:
    tax_rate = 15%
    net_salary = total_salary * 1.15
if tax_status == Head and total_salary >= 5000:
    tax_rate = 25%
    net_salary = total_salary * 1.25
else:
    tax_rate = 19%
    net_salary = total_salary * 1.19

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")