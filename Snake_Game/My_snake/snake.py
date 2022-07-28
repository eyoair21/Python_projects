from turtle import Turtle, Screen

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_state = []
        self.create_snake()
        self.head = self.snake_state[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment(i)

    def add_segment(self,pos):
        new_sqr = Turtle("square")
        new_sqr.color('white')
        new_sqr.penup()
        new_sqr.goto(pos)
        self.snake_state.append(new_sqr)

    def reset(self):
        for seg in self.snake_state:
            seg.goto(1000,1000)
        self.snake_state.clear()
        self.create_snake()
        self.head = self.snake_state[0]

    def extend(self):
        self.add_segment(self.snake_state[-1].position())


    def move_snake(self):
        for seg in range(len(self.snake_state) - 1, 0, -1):
            new_x = self.snake_state[seg - 1].xcor()
            new_y = self.snake_state[seg - 1].ycor()
            self.snake_state[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
