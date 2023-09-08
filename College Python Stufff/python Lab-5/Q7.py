from operator import itemgetter

people_info = []
while True:
    individual_info = input()

    if individual_info == "":
        break
    else:
        people_info.append(tuple((individual_info.split(","))))

people_info.sort(key=itemgetter(0, 1, 2))
print(people_info)
