from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Thiago's Pong")
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with 
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # L
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()