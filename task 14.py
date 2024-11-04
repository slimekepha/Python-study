while True:
    try:
        num1=float(input("Enter the first number:"))
        break
    except ValueError:
        print("Invalid character entered. please enter a valid number")
while True:
    try:
        num2=float(input("Enter the second number:"))
        break
    except ValueError:
        print("Invalid character entered. please enter a valid number")

result=num1+num2
print(f"The sum of {num1} and {num2} is {result}")


