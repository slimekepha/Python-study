
correct_password = "admin@123"
attempts = 0
max_attempts = 4
while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts=attempts+1
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
else:
    print("Account blocked after 4 unsuccessful attempts.")


attemptss=4
password = input("Enter the password: ")
correct_password = "admin@123"
for i in range(attemptss):
    if password==correct_password:
        display="Access granted"
        break
    else:
        remaining_attempts=attemptss-(i+1)
        print(f"incorrect password you have{remaining_attempts}attempts reamaining")
        if remaining_attempts==0:
            display='account blocked'
print(display)
