import random

color = ["Red", "White", "Black", "Green"]
value = random.choice(color)
value1 = random.choices(color, k=8)
value2 = random.random()
value3 = random.uniform(1, 8)
print(value)
print(value1)
print(value2)
print(value3)