namesList = open("./Input/Names/invited_names.txt", "r")
starting_letter = open("./Input/Letters/starting_letter.txt", "r+")
names = [name.strip("\n") for name in namesList.readlines()]
# print(names)
content = starting_letter.read()
# print(content)
for name in names:
    new_content = content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt","w") as file:
        file.write(new_content)

namesList.close()
starting_letter.close()
