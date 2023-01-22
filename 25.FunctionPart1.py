import datetime
def myAge():
    birthYear = int(input("Enter Your Birth Year:"))
    age = datetime.datetime.now().year - birthYear
    print("Your Age is", age , "Years Old")


def myDegree():
    degree = int(input("Enter Your Degree : "))
    if degree >= 90:
        if degree > 94:
            print("A+")
        else:    
            print("A-")
    elif degree >= 80:
        if degree > 84:
            print("B+")
        else:
            print("B-")        
    elif degree >= 70:
        if degree > 74:
            print("C+")
        else:
            print("C-")   
    elif degree >= 60:
        if degree > 64:
            print("D+")
        else:
            print("D-")     
    elif degree >= 50:
        if degree > 54:
            print("E+")
        else:
            print("E-")    
    else:
        print("F") 

def sum():
    return 10+20  

def mySum():
    print(10+20)            

def Sum(a, b):
    return a+b

myAge()
myDegree()
print(sum())
mySum()
print(Sum(5,6))