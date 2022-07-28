from turtle  import Turtle

MOVE_FD = 30
class Paddle(Turtle):
    def __init__(self,postion):
        super(Paddle, self).__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(postion)


    def move_up(self):
        new_Y= self.ycor() + MOVE_FD
        self.goto(self.xcor(),new_Y)

    def move_down(self):
        new_Y = self.ycor() - MOVE_FD
        self.goto(self.xcor(), new_Y)