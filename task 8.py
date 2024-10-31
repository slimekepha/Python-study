
speed = int(input("Enter the speed of the car: "))

if speed < 70:
    print("Ok")
else:
   
    demerit_points = (speed - 70) // 5
    
   
    print(f"Points: {demerit_points}")
    
    if demerit_points > 12:
        print("License suspended")
