transaction_amount = float(input("Enter the transaction amount: "))
account_type=input("enter the account type standard/premium:").capitalize()
if account_type == "Standard":
    if transaction_amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "Premium":
    if transaction_amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print('invalid account type')