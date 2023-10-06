a = ""
for Row in range(0, 7):
    for Col in range(0, 7):
        if ((Row == 0 or Row == 3 or Row == 6) and 1 < Col < 5) or (
                Col == 1 and (Row == 1 or Row == 2 or Row == 6)) or (Col == 5 and (Row == 0 or Row == 4 or Row == 5)):
            a = a + "*"
        else:
            a = a + " "
    a = a + "\n"
print(a)
