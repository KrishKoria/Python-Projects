def Fibb(n):
    if n <= 1:
        return n
    else:
        return Fibb(n - 1) + Fibb(n - 2)


m = int(input("Enter the number: "))
print(f"the fibonacci number is :- {Fibb(m)}")
