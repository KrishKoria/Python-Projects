import random as rd
L = []
for _ in range(10):
    L.append(rd.randint(-100, 100))
print(f"original list :- {L}")
num = [x for x in L if x % 2 != 0]
print(num)