from turtle import *
from paddle import Paddle
from ball import Ball
from time import *
from score import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.title("Play Pong")
screen.tracer(0)
screen.setup(width=800,height=600)
rpad=Paddle((350,0))
lpad=Paddle((-350,0))
ball=Ball()
score=Scoreboard()
screen.listen()
screen.onkeypress(rpad.go_up,"Up")
screen.onkeypress(rpad.go_down,"Down")
screen.onkeypress(lpad.go_up,"w")
screen.onkeypress(lpad.go_down,"s")
gamestate=True
while gamestate:
    sleep(ball.rate)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(rpad)<50 and ball.xcor()>320 or ball.distance(lpad)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_pos()
        score.lpoint()
    if ball.xcor()<-380:
        ball.reset_pos()
        score.rpoint()
screen.exitonclick()