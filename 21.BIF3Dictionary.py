x = {
    1: 'a',
    7: 'b',
    3: 'c',
    6: 'd'
}
y = x.copy()
print(x.items())
print(x.values())
print(x.keys())
print(x.get(7))
x.popitem()
x.pop(3)
print(dict(x))
x.update({2: 's'})
print(dict(x))
x.clear()
print(dict(x))
a = ['a', 'b', 'c']
z = dict.fromkeys(a, 0)
print(dict(z))