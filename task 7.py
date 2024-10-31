marks=int(input("Enter the marks(0-100):"))
if marks <0 or marks >100:
    print("Invalid marks. Please enter marks between 0-100")

if marks>79 and marks<100:
    print("A")
elif marks>=60 and marks<79:
    print("B-")
elif marks>=49 and marks<=59:
    print("C")
elif marks>=40 and marks<=49:
    print("D-")
elif marks<40:
    print("E")