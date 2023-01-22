class A:
    def function1(self):
        print("classA")

class B:
    def function1(self):
        print("classB")

class C(A, B):
    def function1(self):
        print("classC")  

obj1 = A()
obj2 = B()
obj3 = C()
obj1.function1()                      
obj2.function1()                      
obj3.function1()                      