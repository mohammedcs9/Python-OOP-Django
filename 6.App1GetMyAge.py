import datetime

x = datetime.datetime.now().day
print(x)

birthYear = int(input("Enter Your Birth Year:"))
age = datetime.datetime.now().year - birthYear
print("Your Age is", age , "Years Old")