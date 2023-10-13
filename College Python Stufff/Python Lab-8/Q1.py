a = input("Enter a string: ")


def countChar(mystr):
    upperCount = 0
    lowerCount = 0
    for char in mystr:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1

    return [upperCount, lowerCount]


count = countChar(a)
print(f"Upper case characters: {count[0]}")
print(f"Lower case characters: {count[1]}")
