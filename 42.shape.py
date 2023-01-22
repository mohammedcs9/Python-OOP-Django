from PolymorphismShape import Shape, Circle, Rectangle, Square

x = Shape()
x.printVal()

y = Circle()
y.printVal()

z = Rectangle()
z.printVal()

s = Square()
s.printVal()

print(50 * "£")

class A:
    def draw(self, a: Shape):
        a.printVal()

obj = A()
obj.draw(x)        
obj.draw(Shape())        
obj.draw(Circle())        
obj.draw(Rectangle())        
obj.draw(Square())        




