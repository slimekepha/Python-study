math=int(input("enter maths score"))
eng=int(input("enter eng score"))
swa=int(input("enter swa score"))
sci=int(input("enter sci score"))
sos=int(input("enter sos score"))
def calc_totalmarks(math,eng,swa,sci,sos):
    sum=math+eng+swa+sci+sos
    return sum
total_marks=calc_totalmarks(math,eng,swa,sci,sos)
print(total_marks)

def average():
    average_tt=total_marks/5
    return average_tt
total_average=average()
print(total_average)


def find_grade(average):
    if average>79:
        grade='A'
    elif average>60 and average<70:
        grade="B"
    elif average<59 and average>49:
        grade="C-"
    elif average>40 and average<49:
        grade="D-"
    else:
        grade="E"



