import random
import turtle as t

tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range(200):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.color(color)
    tim.fd(30)
    tim.setheading(random.choice(directions))
