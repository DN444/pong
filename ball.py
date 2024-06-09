from turtle import *
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.xmov=10
        self.ymov=10
        self.rate=0.1
    def move(self):
        new_x=self.xcor()+self.xmov
        new_y=self.ycor()+self.ymov
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.ymov*=-1
    def bounce_x(self):
        self.xmov*=-1
        self.rate*=0.9
    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.rate=0.1