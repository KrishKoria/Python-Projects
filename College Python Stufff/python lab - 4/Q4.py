import random as rd
a = []
for _ in range(0, 10):
    a.append(rd.randint(-100, 100))
print(f"Original list is {a}")
rd.shuffle(a)
print(f"Shuffled list is {a}")
