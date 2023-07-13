import art as art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(message, move, method) :
    changed_text = ''
    if method == 'encode' :
        for char in message :
            if char in alphabet:
                position = alphabet.index(char)
                changed_text += alphabet[position + move]
            else :
                changed_text += char
        print(f"The encoded message is {changed_text}")
    elif method == 'decode' :
        for char in message :
            if char in alphabet:
                position = alphabet.index(char)
                changed_text += alphabet[position - move]
            else:
                changed_text += char
        print(f"The decoded message is {changed_text}")
    else :
        print("Wrong Option Entered!!!")


print(art.logo)
end = False
while not end:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    caesar(message=text, move=shift, method=direction)
    choice = input("Do you want to go again, enter yes or no :\n").lower()
    if choice == "no":
        print("Thank you for using Cypher Application")
        end = True
