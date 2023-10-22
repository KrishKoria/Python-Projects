def printInteger(roman):
    value = [1000, 900, 500, 400,
             100, 90, 50, 40,
             10, 9, 5, 4,
             1]
    symbol = ["M", "CM", "D", "CD",
              "C", "XC", "L", "XL",
              "X", "IX", "V", "IV",
              "I"]
    num = 0
    for i in range(len(roman)):
        if i > 0 and value[symbol.index(roman[i])] > value[symbol.index(roman[i - 1])]:
            num += value[symbol.index(roman[i])] - 2 * value[symbol.index(roman[i - 1])]
        else:
            num += value[symbol.index(roman[i])]

    print(num)


a = input("Enter the roman number: ")
printInteger(a)
