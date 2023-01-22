from enum import Enum

class Animal(Enum):
    DOG = 6
    CAT = 2
    LION = 3

print(Animal.DOG)
print(Animal(6))
print(Animal["DOG"])
print(Animal.DOG.name)
print(Animal.DOG.value)
print(repr(Animal.DOG))

print(50 * "£")

for i in Animal:
    print(i)

print(50 * "£")

for i in Animal:
    print(repr(i))    

print(50 * "£")

d = {}
d[Animal.DOG] = 33
d[Animal.CAT] = 43
d[Animal.LION] = 53
print(dict(d))