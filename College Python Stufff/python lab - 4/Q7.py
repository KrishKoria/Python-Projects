a = [1, 2, 3, 4]
myString = "emp"
for i in range(0, len(a)):
    new_val = myString + str(a[i])
    a[i] = new_val
print(f"Updated string is {a}")
