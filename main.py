from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen = Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong game")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.update()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.update()

game_is_on = True

ball_speed = 0.1
while game_is_on:
    time.sleep(ball_speed)
    scoreboard.show()
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball_speed *= 0.9
    if ball.xcor() >= 400:
        ball.start()
        ball_speed = 0.1
        scoreboard.left_score += 1
    if ball.xcor() <= -400:
        ball.start()
        ball_speed = 0.1
        scoreboard.right_score += 1
screen.exitonclick()
