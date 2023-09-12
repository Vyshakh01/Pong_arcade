import turtle
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard
from middleline import Line
screen=turtle.Screen()
screen.setup(width=750,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

line=Line()

screen.listen()

screen.onkeypress(fun=r_paddle.up,key="Up")
screen.onkeypress(fun=r_paddle.down,key="Down")
screen.onkeypress(fun=l_paddle.up,key="w")
screen.onkeypress(fun=l_paddle.down,key="s")
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor()>390:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor()<-390:
        ball.reset()
        scoreboard.r_point()
    if scoreboard.l_score>10:
        scoreboard.gameover("left side")
        is_game_on=False
    elif scoreboard.r_score>10:
        scoreboard.gameover("right side")
        is_game_on=False






screen.exitonclick()
