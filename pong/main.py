from turtle import Screen,Turtle
from paddles import Paddles
from ball import Ball
import time
from scoreboard import Scoreboard
from net import Net
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
score=Scoreboard()
r_paddle= Paddles((350, 0))
l_paddle= Paddles((-350, 0))
ball=Ball()
net=Net()
speed=0.1

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(l_paddle.go_up,"w")
screen.onkey(key="s",fun=l_paddle.go_down)

game_is_on=True
while game_is_on:
    time.sleep(speed)
    screen.update()
    net.draw_the_line()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or  ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.hit_paddle()
        speed*=0.9
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.reretpos()
        score.point_left()
        speed=0.1

    if ball.xcor()<-380:
        ball.reretpos()
        score.point_right()
        speed=0.1

screen.exitonclick()