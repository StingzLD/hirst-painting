import random
import colorgram
import turtle


# Extract colors from image
def extract_colors(image, num_colors):
    rgb_colors = []
    colors = colorgram.extract(image, num_colors)
    for color in colors:
        if color.rgb.r < 240 and color.rgb.g < 240 and color.rgb.b < 240:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            rgb = (r, g, b)
            rgb_colors.append(rgb)
    return rgb_colors


# Create a new dot of a random color then move to the next position
def add_dot():
    dog.dot(20, random.choice(color_list))
    dog.forward(50)


# Move position to the beginning of the next line
def next_line(line):
    y = -250 + (line * 50)
    dog.setposition(-250, y)
    dog.setheading(0)


# Set color mode to RGB
turtle.colormode(255)

# Create turtle object
dog = turtle.Turtle()
dog.hideturtle()
dog.penup()
dog.speed("fastest")
dog.setposition(-250, -250)

# Extract colors from image
color_list = extract_colors('image.jpg', 30)

# Create painting
row = 0
num_dots = 100
for dot_count in range(1, num_dots + 1):
    add_dot()
    if dot_count % 10 == 0:
        row += 1
        next_line(row)

# Keep window open until clicked on
screen = turtle.Screen()
screen.exitonclick()
