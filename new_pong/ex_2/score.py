from paddle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 255)
        self.write(f"{self.l_score}    {self.r_right}", align='center', font=('Courier', 35, 'normal'))

    def score_lef(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}    {self.r_right}", align='center', font=('Courier', 35, 'normal'))


    def score_right(self):
        self.r_right += 1
        self.clear()
        self.write(f"{self.l_score}    {self.r_right}", align='center', font=('Courier', 35, 'normal'))
