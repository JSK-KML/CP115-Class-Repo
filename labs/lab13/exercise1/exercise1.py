correct_password = "python123"

# TODO: Your code here
login_successful = False
attempts_used = 0

while attempts_used <= 3:
    password = input("Enter password: ")
    attempts_used += 1

    if password == correct_password:
        login_successful = True
        break
    else:
        continue

print(login_successful)
print(attempts_used)

