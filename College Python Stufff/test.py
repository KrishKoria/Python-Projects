def RabbitAndChicken(heads, legs):
    for i in range(heads + 1):
        if (i * 4) + ((heads - i) * 2) == legs:
            return i, heads - i
    return "No Solution"


print(RabbitAndChicken(35, 94))
