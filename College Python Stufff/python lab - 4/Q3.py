import random as rd
a = []
for _ in range(0, 10):
    a.append(rd.randint(-100, 100))
print(f"The current list is {a}")
a.pop(0)
a.pop(3)
a.pop(3)
print(f"The changed list is {a}")
