from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


# set screen background
screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.tracer(0)

# create paddle, ball, scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()


# Detect key inputs
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, 's')


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # ball collide with the top or bottom plate
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # ball collide with paddle
    if ball.xcor() > 335 and ball.distance(r_paddle) < 50 or ball.xcor() < -335 and ball.distance(l_paddle) < 50:
        ball.x_bounce()
    # ball pass paddle score
    if ball.xcor() > 370 and ball.distance(r_paddle) > 50:
        ball.respostion()
        score.score_lef()

    if ball.xcor() < -370 and ball.distance(l_paddle) > 50:
        ball.respostion()
        score.score_right()

screen.exitonclick()
