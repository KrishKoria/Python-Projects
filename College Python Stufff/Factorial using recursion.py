def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number :- "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial is", factorial(num))

# O(n) but slower for bigger values due to larger overhead in recursion
