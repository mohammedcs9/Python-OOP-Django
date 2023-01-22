class A: #indirect super class
    age: int

    def info(self):
        self.age = 10
        print(" Age =", self.age)

class B(A): #direct super class
    def info2(self):
        super().info()

class C(B): #sub class
    def info3(self):
        print("Hello")        

a1 = C()       
a1.info2()
