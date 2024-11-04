studentscore = int(input("Enter the student's score: "))
studentattendance = int(input("Enter the student's attendance: "))

if studentscore>90:
    if studentattendance >80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
    print("Student score is not greater than 90")