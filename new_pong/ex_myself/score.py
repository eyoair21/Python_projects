from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier',30,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.update_wrt()

    def update_wrt(self):
        self.clear()
        self.goto(0,240)
        self.write(f"{self.lscore}        {self.rscore}", align=ALIGN, font=FONT)

    def left_score(self):
        self.lscore += 1
        self.update_wrt()

    def right_score(self):
        self.rscore += 1
        self.update_wrt()