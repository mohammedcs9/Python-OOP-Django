x = [2, 8, 2, 9, 6, 2]
y = x.copy()
print("list(x)", list(x))
print("list(y)", list(y))
print("x.count(2) =", x.count(2))
x.append(3)
print("list(x)", list(x))
x.insert(2, 3)
print("list(x)", list(x))
x.remove(2)
print("list(x)", list(x))
x.pop(2)
print("list(x)", list(x))
print("x.index(3) =", x.index(3))
x.extend(y)
print("list(x)", list(x))
x.clear()
print("list(x)", list(x))
z = (2, 7, 4, 7, 7)
print("z.count(7) =", z.count(7))
print("z.index(4) =", z.index(4))
print("tuple(z) =", tuple(z))