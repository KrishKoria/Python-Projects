import random as rd
a = []
for _ in range(0, 10):
    a.append(rd.randint(-100, 100))

print(f"Original list 1 is {a}")

b = []
for _ in range(0, 10):
    b.append(rd.randint(0, 200))

print(f"Original list 2 is {b}")

a[len(a):] = b

print(f"Extended list 1 is {a}")