x = open("test.txt", "w")
x.write("Mohmmad\n")
x.close()

x = open("test.txt", "a")
x.write("Nabeel\n")
x.write("Alzoubi")
x.close()

x = open("test.txt", "r")
for i in x:
    print(i)
x.close()