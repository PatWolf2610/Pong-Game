import imp
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
PADDLE_RIGHT_ORG_POS = (560,0)
PADDLE_LEFT_ORG_POS = (-570,0)


screen  = Screen()

screen.setup(width=1200,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
paddle_right = Paddle(PADDLE_RIGHT_ORG_POS)
paddle_left = Paddle(PADDLE_LEFT_ORG_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up',fun=paddle_right.go_up)
screen.onkey(key='Down',fun=paddle_right.go_down)
screen.onkey(key='w',fun=paddle_left.go_up)
screen.onkey(key='s',fun=paddle_left.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_delay)  #pause tenscreen to see the ball
    ball.ball_move()

    #detect collision with top and bottom and boucing

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()
    
    #detect collision with paddle and bouncing
    if ball.distance(paddle_right) < 35 and ball.xcor()>505:
        ball.paddle_bounce()
    
    if ball.distance(paddle_left) <35 and ball.xcor()<-485:
        ball.paddle_bounce()

    # goal score
    if ball.xcor() > 570:
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor() < -580:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()