# 5
li = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]
x = []
for i in li:
    x.append(i[0])
    x.append(i[1])
print(x)
# 6
li = [1, 2, 3, 4, 5, 6, 7, 1, 2]
s = set()
for i in li:
    s.add(li[i])
print(s)

# 7
li = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]
for i in range(0, len(li)):
    x = list(li[i])
    x[len(x) - 1] = 'x'
    li[i] = tuple(x)
print(li)
# 8
d1 = {1: 3, 3: 5, 2: 5, 7: 8}
d2 = {1: 2, 2: 4, 9: 0, 6: 9}
d1.update(d2)
print(d1)
# 9
dict = {}
li = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]
for i in li:
    dict[i[0]] = i[1]
print(dict)
# 10
d1 = {1: 3, 3: 5, 2: 5, 7: 8}
print(d1.items())
print(d1.values())
print(d1.keys())
