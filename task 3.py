phone_number = input("Enter your phone number: ")
def validate_and_convert_phone_number(phone_number):
    if phone_number.startswith("+254"):
        return phone_number
    elif phone_number.startswith("07"):
        return "+254" + phone_number[1:]
    elif phone_number.startswith("7"):
        return "+254" + phone_number
    elif phone_number.startswith("254"):
        return "+" + phone_number
    elif phone_number.startswith("01"):
        return "+254" + phone_number[1:]
    elif phone_number.startswith("1"):
        return "+254" + phone_number
    else:
        return "Invalid phone number format"

converted_phone_number = validate_and_convert_phone_number(phone_number)
print(converted_phone_number)

