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


