from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))
ball = Ball()
gm_score = ScoreBoard()


screen.listen()
screen.onkey(lpaddle.move_up,'w')
screen.onkey(lpaddle.move_down,'s')
screen.onkey(rpaddle.move_up,'Up')
screen.onkey(rpaddle.move_down,'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.ball_edge()

    if ball.distance(lpaddle) < 50 and ball.xcor() < -330 or ball.distance(rpaddle) < 50 and ball.xcor() > 330:
        ball.ball_paddle()

    if ball.xcor() > 360:
        gm_score.left_score()
        ball.ball_reset()

    if ball.xcor() < -360:
        gm_score.right_score()
        ball.ball_reset()



screen.exitonclick()