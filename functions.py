def rectangle_area():
    length=40
    width=12
    area=(length*width)
    print(area)

rectangle_area()

def area_rect(len,width):
    area=len*width
    print(area)


area_rect(20,10)

def area_triangle(base,height):
    area=base*height/2
    print(area)

area_triangle(10,7)




def check_even_odd():
    num=int(input("Enter the number:"))

    if num%2==0:
        print("Number is even")
    
    else:
        print("Number is odd")

check_even_odd()




def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest_number = find_largest(num1, num2, num3)

print(f"The largest number is: {largest_number}")
