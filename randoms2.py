class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def identify(self):
        print(f"name is {self.name} and my age is {self.age}")
idt=Person("Hazel",23)
idt.identify()

def calculation(num1,num2):
    addition=num1+num2
    subraction=num1-num2
    return addition, subraction
total=calculation(80,40)
print(total)


def show_employee(name,salary=5000):
    print('name:',name, 'salary:',salary)
 
 
show_employee('hazel',7000)
show_employee('don')


name=str(input("Enter your name:"))
salary=int(input("Enter the number:"))
def employee_details():
    if salary>=40000:
        print("you are eligible")
    else:
        print("you are not eligible")
employee_details()

