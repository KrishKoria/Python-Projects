year = int(input("Enter the year :- "))
if year % 400 == 0:
    print(f"the year {year} is a leap year")
elif year % 4 == 0:
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")
