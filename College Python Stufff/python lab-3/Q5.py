digitcount = 0
lettercount = 0

a = input("Enter a String :- ")
for char in a:
    if char.isdigit():
        digitcount += 1
    elif char.isalpha():
        lettercount += 1
    else:
        pass

print(f"The String {a} has {digitcount} digits and {lettercount} letters")
