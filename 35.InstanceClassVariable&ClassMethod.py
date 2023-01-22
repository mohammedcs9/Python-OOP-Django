class Human:
    s1 = 0 # class variable

    def info(self, p_name, p_length, p_age): 
        self.name = p_name
        self.length = p_length
        self.age = p_age
        print("Name =", self.name)
        print("Length =", self.length)
        print("Age =", self.age)

h1 = Human()
h2 = Human()
h1.info("ahmed", 180, 20)
print(h1.name)
print(Human.s1)
h1.info("mohmmad", 170, 25)

print(50*"£")

class Human:
    @classmethod # class method
    def classinfo(cls): 
        print("Hello")

    def info(self, p_name, p_length, p_age): 
        self.name = p_name
        self.length = p_length
        self.age = p_age
        print("Name =", self.name)
        print("Length =", self.length)
        print("Age =", self.age)

Human.classinfo()
h1 = Human()
h2 = Human()
h1.info("ahmed", 180, 20)
h2.info("mohmmad", 170, 25)

print(50*"£")

class Human:

    def info(self, p_name, p_length, p_age): 
        self.name = p_name
        self.length = p_length
        self.age = p_age
        print("Name =", self.name)
        print("Length =", self.length)
        print("Age =", self.age)


h1 = Human()
h2 = Human()
Human.info(h1,"ahmed", 180, 20)
Human.info(h2,"mohmmad", 170, 25)

print(50*"£")

class ClassA:

    def classA(self, p_name): 
        print("Name =", p_name)

class ClassB:

    def classB(self, p_name): 
        print("Name =", p_name)        
        

h1 = ClassA()
h2 = ClassB()
h1.classA("Ali")
h2.classB("Ahmed")