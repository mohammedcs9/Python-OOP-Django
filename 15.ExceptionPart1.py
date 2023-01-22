while True:
    try:
        age = int(input("Enter Your Age: "))
        print("Your Age Is", age,"Years Old")
        break
    except Exception as ex:
        print("You Entered Wrong Value") 