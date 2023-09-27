def createList():
    return [i ** 2 for i in range(1, 21)]


myList = createList()
for i in range(6):
    print(myList[i], end=" ")
