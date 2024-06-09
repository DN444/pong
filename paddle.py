from turtle import *
class Paddle(Turtle):
    def __init__(self,tup):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(tup)
    def go_up(self):
        y=self.ycor()
        y+=20
        self.sety(y)
    def go_down(self):
        y=self.ycor()
        y-=20
        self.sety(y)