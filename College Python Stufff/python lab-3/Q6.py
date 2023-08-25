a = ""
for Row in range(0, 7):
    for Col in range(0, 7):
        if ((Row == 0 or Row == 6) and 0 <= Col <= 6) or Row + Col == 6:
            a = a + "*"
        else:
            a = a + " "
    a = a + "\n"
print(a)
