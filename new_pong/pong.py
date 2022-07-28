from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping - Pong ")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # detect misses
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_pos()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_pos()



screen.exitonclick()
