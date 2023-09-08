freq = {}  # frequency of words in text
line = input("Enter Text:")
for word in line.split():
    freq[word] = freq.get(word, 0) + 1

words = freq.keys()
sorted_words = sorted(words)

print("Frequency chart")
for w in sorted_words:
    print(f"{w}:{freq[w]}")