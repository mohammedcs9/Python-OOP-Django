class A:
    x: int
    def myFun1(self):
        print("NumberA =", self.x)

    class B:
        y: int

        def myFun2(self):
            print("NumberB =", self.y)    

a = A()
a.x = 10
a.myFun1()

b = A.B()
b.y = 20
b.myFun2()            

print(50 * "£")

def a():
    class C:
        r: int

        def myFun3(self):
            print("NumberC =", self.r) 

    z = C() 
    z.r = 30
    z.myFun3()

a()                                   

