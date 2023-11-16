import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

distance = 20

game_on_flag = True

snake = Snake()

screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')

while game_on_flag:
    screen.update()
    time.sleep(0.1)
    snake.move(distance)

screen.exitonclick()
