def printRoman(num):
    if num > 3999:
        print("Number should be less than 4000")
        return
    value = [1000, 900, 500, 400,
             100, 90, 50, 40,
             10, 9, 5, 4,
             1]
    symbol = ["M", "CM", "D", "CD",
              "C", "XC", "L", "XL",
              "X", "IX", "V", "IV",
              "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // value[i]):
            roman_num += symbol[i]
            num -= value[i]
        i += 1
    print(roman_num)


a = int(input("Enter the number: "))
printRoman(a)
