from math import sqrt


def value(n):
    c = 50
    h = 30
    return round(sqrt((2 * c * n) / h))


d = input("Enter values seperated by ',' :- ").split(',')
for num in d:
    print(value(int(num)), end=',')
