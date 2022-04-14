import random

x = set()
x.add(1)
print(x)
x.add(1)
x.add(2)
x = list(x)
print(x)
print(random.choice(x))