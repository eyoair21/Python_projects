from turtle import Turtle

ALIGN = "center"
FONT = ('Cambria', 25, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read()) # convert string to integer
        self.color('white')
        self.penup()
        self.hideturtle()
        self.cur_res()

    def cur_res(self):
        self.goto(0, 225)
        self.clear()
        self.write(f"Score: {self.score}    High-Score:{self.high_score}", align=ALIGN, font=FONT)

    def new_score(self):
        self.score += 1
        self.cur_res()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.cur_res()

  # #def over(self):
   #     self.goto(0,0)
   #     self.color('red')
   #     self.write("GAME OVER !!!!", align=ALIGN, font=FONT)



