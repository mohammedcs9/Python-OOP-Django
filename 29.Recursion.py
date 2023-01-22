def add(a):
    if a != 0:
        return a+add(a-1)
    else:
        return 0

x = int(input("Enter A Number:"))
print("Sum =", add(x))            