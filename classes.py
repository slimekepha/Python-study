# define a class named car

class car:
    def __init__(self,colour,brand,shape):
        self.colour=colour
        self.brand=brand
        self.shape=shape
    
    def describe(self):
        return f"the clour of the car is {self.colour} the brand is {self.brand} and shape is {self.shape}"
    

mycar=car('red','audi','wagon')
print(mycar.describe())
print(mycar.brand)


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def describe(self):
        return f"Hello my name is {self.name} and am {self.age} years old"
std=Student('Hazel','21')
print(std.describe())





class Calculator:
    
    def add(self,num1, num2):
        return num1 + num2
    
   
    def subtract(self, num1, num2):
        return num1 - num2
    
    
    def multiply(self, num1, num2):
        return num1 * num2
    
   
    def divide(self,num1,num2):
         return num1 / num2
        

calc = Calculator()

print("Addition of 10 and 5:", calc.add(10, 5))
print("Subtraction of 10 and 5:", calc.subtract(10, 5))
print("Multiplication of 10 and 5:", calc.multiply(10, 5))
print("Division of 10 by 5:", calc.divide(10, 5))
print("Division of 10 by 0:", calc.divide(10, 5))
