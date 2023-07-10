from art import logo
import os

print(logo)


def add(n1, n2) :
    return n1 + n2


def sub(n1, n2) :
    return n1 - n2


def multiply(n1, n2) :
    return n1 * n2


def divide(n1, n2) :
    if n2 != 0 :
        return n1 / n2


# approach below is ok for normal calculator but not ok for chaining operations
# stop = False
# new_num = True
# a = float(input("Enter the First Number :- "))
# b = float(input("Enter the Second Number :- "))
# while not stop :
#     if not new_num:
#         print("1) Add")
#         print("2) Subtract")
#         print("3) Multiply")
#         print("4) Divide")
#         print("5) Exit")
#         choice = int(input("What do you want to do,Enter 1,2,3,4 or 5 :- "))
#         if choice == 1 :
#             c = add(a, b)
#             print(f"The Sum of {a} and {b} is {c}")
#         elif choice == 2 :
#             c = sub(a, b)
#             print(f"The Subtraction of {a} and {b} is {c}")
#         elif choice == 3 :
#             c = multiply(a, b)
#             print(f"The Multiplication of {a} and {b} is {c}")
#         elif choice == 4 :
#             if b == 0 :
#                 print("Division By 0 cannot Take Place!!!")
#             else :
#                 c = divide(a, b)
#                 print(f"The Division of {a} and {b} is {c}")
#         elif choice == 5 :
#             stop = True
#             print("Thank You for using Calculator")
#
#         else :
#             print("Wrong Choice Entered,Try Again!!")
#
#         new_choice = input(f"Continue with {c} or take a new number, enter y to continue or n for new calculation").lower()
#         if new_choice == 'y':
#             continue
#         elif new_choice == 'n':
#             new_num = False
#         else:
#             print("Wrong Option Entered")
#     else:
#

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,
}


def calculator() :
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations :
        print(symbol)
    should_continue = True

    while should_continue :
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y' :
            num1 = answer
        else :
            should_continue = False
            os.system("cls")
            calculator()


calculator()
