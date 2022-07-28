from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My - Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

get_val = True
while get_val:
    screen.update()
    time.sleep(0.07)
    snake.move_snake()


# detect food contact
    if snake.head.distance(food) < 25:
        food.referesh()
        score.new_score()
        snake.extend()

# Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()

# detect collision with tail
    for seg in snake.snake_state[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
