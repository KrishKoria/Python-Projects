from math import sqrt,pow
movement_info = []
while True:
    steps = input()
    if steps == "":
        break
    else:
        movement_info.append(tuple((steps.split())))

# print(movement_info)
pos = [0, 0]
for movement in movement_info:
    if movement[0] == "UP":
        pos[1] = pos[1] + int(movement[1])
    if movement[0] == "DOWN":
        pos[1] = pos[1] - int(movement[1])
    if movement[0] == "LEFT":
        pos[0] = pos[0] + int(movement[1])
    if movement[0] == "RIGHT":
        pos[0] = pos[0] - int(movement[1])

# print(initial_pos)

distance = sqrt(pow(pos[0], 2) + pow(pos[1], 2))
print(f"The distance from origin is {round(distance)}")
