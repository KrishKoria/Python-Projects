words = input("enter words sep by ',' ").split(',')
print("Sorted words are :- ")
for word in sorted(words):
    print(word, end=',')
