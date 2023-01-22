class myclass:

    def __init__(self, name): #Constructor
        print(name)   

m1 = myclass("Hello")

class Human:
    def __init__(self, p_name, p_length, p_age): #Constructor
        self.name = p_name
        self.length = p_length
        self.age = p_age
        print("Name =", self.name)
        print("Length =", self.length)
        print("Age =", self.age)

h1 = Human("ahmed", 180, 20)
h2 = Human("mohmmad", 170, 25)
