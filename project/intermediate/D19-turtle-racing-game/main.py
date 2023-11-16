import random
from turtle import Turtle, Screen

start_flag = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Make your bet', "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []
x = -230
y = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    y += 20
    new_turtle.goto(x=x, y=y)
    all_turtles.append(new_turtle)

if user_bet:
    start_flag = True

while start_flag:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            start_flag = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won the race, the {winning_color} turtle wins")
            else:
                print(f"you've lost the race, the {winning_color} turtle wins")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
