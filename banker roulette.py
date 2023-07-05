import random as rd

names_string = input("Enter names seperated by comma :- ")
names = names_string.split(", ")

##print(names[rd.randint(0, len(names)-1)], "is going to buy the meal today")

print(rd.choice(names))
