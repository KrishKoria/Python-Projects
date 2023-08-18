# Q1
import sys

print(sys.version)

# Q2
CURRENT_YEAR = 2023
name = input("Enter Your Name :- ")
age = int(input("Enter your Age :- "))
turn100 = (CURRENT_YEAR - age) + 100
print(f"{name}, you will turn 100 in year {turn100}")


# Q3
import math

radius = float(input("Enter a radius :- "))
print(f"The area of the circle is :- {math.pi * radius * radius}")

# Q4
num = int(input("Enter a Number :- "))
if num % 2 == 0:
    print(f"The {num} is EVEN")
else:
    print(f"The {num} is ODD")

# Q5
user_in = input("Enter a String :- ")
if user_in == user_in[::-1]:
    print(f"The String {user_in} is a palindrome")
else:
    print(f"The String {user_in} is not a palindrome")


# Q6
strings = input("Enter two strings seperated by space :- ").lower().split()
new_a = strings[1][:2] + strings[0][2:]
new_b = strings[0][:2] + strings[1][2:]

print(f"The Strings are :- {new_a} and {new_b}")


# Q7
a = input("Enter a string :- ")
if len(a) < 3:
    print(f"The String is {a}")
elif a[-3:] == "ing":
    print(f"The String is {a}ly")
else:
    print(f"The String is {a}ing")

# Q8
a = input("Enter a String :- ")
b = a[-1] + a[1:-1] + a[0]
print(f"The exchanged String is {b}")

# Q9
a = input("Enter a String :- ")
rep = a.replace(a[0], '$')
print(a[0] + rep[1:])

# Q10
a = input("Enter A String :- ")
print(f"UPPERCASE is :- {a.upper()}")
print(f"lowercase is :- {a.lower()}")
