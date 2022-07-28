from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food catch
    if snake.head.distance(food) < 20:
        food.new_postion()
        snake.extend()
        score_board.incrs_score()
        print("yum yum")

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_board.end_game()
        game_on = False

    #tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 6:
            game_on = False
            score_board.end_game()








screen.exitonclick()