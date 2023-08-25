choice = int(input("Enter 1 for celsius to fahrenheit or 0 for fahrenheit to celsius :- "))

if choice == 1:
    temp = float(input("Enter temp in celsius :- "))
    f = (1.8 * temp) + 32
    print(f"Temperature in fahrenheit is :-  {f}")
elif choice == 0:
    temp = float(input("Enter temp in fahrenheit :- "))
    c = (temp-32) * (5/9)
    print(f"Temperature in Celsius is :-  {c}")
else:
    print("Wrong Option entered!")
