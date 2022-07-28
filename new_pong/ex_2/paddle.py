from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(postion)


    def move_up(self):
        new_yr = self.ycor() + 25
        self.goto(self.xcor(), new_yr)


    def move_down(self):
        new_yr = self.ycor() - 25
        self.goto(self.xcor(), new_yr)


