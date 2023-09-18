from random import randrange
mydict = {}
for i in range(10):
    mydict['key'+str(i)] = randrange(10)

print(max(mydict.values()))
print(min(mydict.values()))
