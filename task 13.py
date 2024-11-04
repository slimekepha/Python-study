correct_email="admin@mail.com"
correct_password="Admin@123"
attempts=0
max_attempts=3
while attempts<max_attempts:
    email=input("Enter the email:")
    password=input("Enter the password:")
    

    if password==correct_password and email==correct_email:
        print("Access granted")
        break
    else:
        remaining_attempts=attempts+1
        print(f"Invalid password or email you have{max_attempts-attempts} left.")
else:
    print("Account blocked after 3 attempts")


   

    



