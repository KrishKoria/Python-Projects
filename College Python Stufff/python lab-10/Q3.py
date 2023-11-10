import re


def extract_digits_words(sentence):
    digit_words = re.findall(r'\b\d+\b', sentence)
    return digit_words


input_sentence = input("Enter a sequence of words: ")

result = extract_digits_words(input_sentence)

if result:
    print(result)
else:
    print("No words composed of digits found.")
