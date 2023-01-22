for x in range(10):
    print("x = ", x)
    if x == 3:
        continue

for i in range(10):
    for j in range(10):
        print(i+1, "*", j+1, "=", (i+1)*(j+1))
        if j == 3:
            #break
            continue
    if i == 4:
        break

