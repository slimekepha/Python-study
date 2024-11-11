class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound=sound
    
    def describe(self):
        return f"The {self.species} goes {self.sound}!!"

the_animal=Animal('panthera','raar')
print(the_animal.describe())
print(the_animal.species)


class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    
    def describe(self):
        return f'Title of the book is {self.title}, it was written by {self.author} on the year {self.year}'
    
des_book=Book('Heroes of Olympus','Rick Riodarn','2013')
print(des_book.describe())



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return f"Withdrawal denied. Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
    
    def get_balance(self):
        return f"Current balance: {self.balance}"

account = BankAccount("John Doe")

print(account.deposit(1000))
print(account.withdraw(500))
print(account.withdraw(600))
print(account.get_balance())


class Rectangle:
    
    def area(self,width,height):
        return width*height
    def perimeter(self,width,height):
        return 2*(width+height)

result=Rectangle()
print(result.area(10,20))
print(result.perimeter(20,30))




class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def give_raise(self,percentage):
        self.salary+= self.salary*(percentage/100)
        return self.salary
    
emp_details=Employee('Hazel',60000)
emp_details.give_raise(10)
print(f"hello {emp_details.name}, your new salary is {emp_details.salary}")




class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def honk(self):
        return f"{self.brand} {self.model} goes 'Honk honk!'"

class Motorcycle(Vehicle):
    def rev_engine(self):
        return f"{self.brand} {self.model} goes 'Vroom vroom!'"

car = Car("Toyota", "Corolla")
print(car.honk())

motorcycle = Motorcycle("Harley-Davidson", "Sportster")
print(motorcycle.rev_engine())
