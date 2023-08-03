import colorgram as cg

color_list = []
colors = cg.extract("image.jpg", 30)
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

print(color_list)
