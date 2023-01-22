def function1():
    print("Hello From My Function1")
lambda1 = lambda :print("Hello From My Function1")

def function2(a):
    print(a*a)
lambda2 = lambda a:print(a*a)

def function3():
    return "Hello From My Function3"
lambda3 = lambda :"Hello From My Function3"

def function4(a):
    return a*a
lambda4 = lambda a:a*a   

function1()
lambda1()
function2(5)
lambda2(5)
print(function3())
print(lambda3())
print(function4(4))
print(lambda4(4))
