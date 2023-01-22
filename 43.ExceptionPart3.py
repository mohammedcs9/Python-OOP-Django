def draw(a):
    ex = Exception()
    try:
        if a < 0:
            raise ex

    except Exception as e:
        print("You Entered A Negative Value..")        
    print("Number =", a)

draw(-10)  

print(50 * "£")

def draw1(b):
    ex1 = Exception()
    if b < 0:
        raise ex1
    print("Number =", b)    

try:
    draw1(-10)             
except Exception as e1:
    print("You Entered A Negative Value..")    
