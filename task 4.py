email = input("Enter your email address: ")

def validate_email(email):
    if "@" in email and "." in email:
        return "Valid email"
    else:
        return "Invalid email"



validation_result = validate_email(email)

print(validation_result)
