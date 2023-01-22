def sum1(a, b):
    total = a+b
    print("Sum =", total)
sum2 = lambda a, b:print("Sum =", a+b)    

def hof(x, y, z):
    z(x, y) #sum(3,5)

hof(3, 5, sum1)  
hof(3, 5, sum2)  