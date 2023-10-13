def Frequency(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


a = input("Enter a String :- ")

frequency = Frequency(a)
for i in sorted(frequency.keys()):
    print(f"{i} : {frequency[i]}")
