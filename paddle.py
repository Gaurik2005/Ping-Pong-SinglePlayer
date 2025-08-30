from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.goto(0,-270)

    def move_right(self):
        self.goto(self.xcor()+40,self.ycor())

    def move_left(self):
        self.goto(self.xcor()-40,self.ycor())

    def reset_paddle(self):
        self.goto(0,-270)