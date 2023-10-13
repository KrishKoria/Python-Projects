def uniqueList(mylist):
    newList = []
    for i in mylist:
        if i not in newList:
            newList.append(i)

    return newList


a = list(input("Enter a list seperated by comma :- ").split(","))
print(uniqueList(a))
