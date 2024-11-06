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
