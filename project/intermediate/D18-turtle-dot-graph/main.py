import random
import turtle
from turtle import Turtle, Screen
import colorgram

# colors = colorgram.extract('hirst_dots.jpg', 20)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list=[(236, 236, 242), (240, 229, 236), (241, 231, 220), (224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61), (22, 114, 140), (58, 46, 35), (244, 197, 53), (194, 138, 160), (60, 136, 75), (225, 83, 45), (230, 174, 191), (28, 61, 53), (58, 71, 38), (155, 188, 179)]


def turtle_draw_hirst():
    tim = Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for dot_count in range(1, 101):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

def turtle_draw_random():
    tim = Turtle()

    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    directions = [0, 90, 180, 270]
    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


def turtle_draw_geometry():
    timmy = Turtle()
    for num in range(3, 11):
        angle = round(360 / num)
        for _ in range(num):
            timmy.forward(100)
            timmy.right(angle)


def turtle_draw_square():
    tim = Turtle()

    tim.shape('turtle')
    tim.color('red')
    for _ in range(4):
        for _ in range(15):
            tim.forward(10)
            tim.penup()
            tim.forward(10)
            tim.pendown()
        tim.right(90)


screen = Screen()
screen.colormode(255)
turtle_draw_hirst()
screen.exitonclick()
