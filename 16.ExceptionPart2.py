while True:
    try:
        x = int(input("Enter Your Age 1:"))
        y = int(input("Enter Your Age 2:"))
        print("Div =", x/y)
        break
    except ValueError as ex:
        print("Please, Enter Number")
    except ZeroDivisionError as ex:
        print("Please, Don't Divide Number By Zero")