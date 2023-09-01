import random as rd
a = []
summation = 0
for _ in range(0, 10):
    a.append(rd.randint(-100, 100))

for num in a:
    summation += num

print(f"Sum is {summation}")
