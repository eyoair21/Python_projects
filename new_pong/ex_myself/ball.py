
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.x_dir = 10
        self.y_dir = 10
        self.speed_rt = 0.3
        self.goto(0,0)
        self.penup()

    def ball_move(self):
        x_dir = self.xcor() + self.x_dir
        y_dir = self.ycor() + self.y_dir
        self.goto(x_dir,y_dir)

    def ball_edge(self):
        self.y_dir  *= -1
        y_dir = self.ycor() + self.y_dir
        self.goto(self.xcor(), y_dir)

    def ball_paddle(self):

        self.x_dir = self.x_dir + (self.x_dir * self.speed_rt)
        self.x_dir *= -1
        x_dir = self.xcor() + self.x_dir
        self.goto(x_dir, self.ycor())

    def ball_reset(self):
        self.goto(0,0)
        self.clear()
        self.x_dir = 10