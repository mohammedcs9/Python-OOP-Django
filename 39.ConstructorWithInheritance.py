class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

class Student(Person):
    def __init__(self, x, y): # Constructor
        super().__init__(x,  y)        

obj1 = Student("mohmmad", 22)
print(obj1.name)
print(obj1.age)

print(50*"£")

class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

class Student(Person):
    def myFun(self): 
        print("Hello")      

obj1 = Student("mohmmad", 22)
print(obj1.name)
print(obj1.age)