cube = float(input())
epsilon = 0.001
low, high = 0, cube
guess = (low + high) / 2

while True:
    if abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    else:
        break

print(f"cube root is {round(guess)}")