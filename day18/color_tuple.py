#this was downloaded from the class.

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
#    rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    found_color = (r, g, b)
    rgb_colors.append(found_color)

print(rgb_colors)
