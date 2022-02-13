from turtle import Screen
from paddle import Paddle
from ball import Ball
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

screen.listen()
screen.onkey(key='Up',fun=paddle_right.go_up)
screen.onkey(key='Down',fun=paddle_right.go_down)
screen.onkey(key='w',fun=paddle_left.go_up)
screen.onkey(key='s',fun=paddle_left.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  #pause tenscreen to see the ball
    ball.ball_move()

    #detect collision with top and bottom and boucing
    # the top
    if ball.ycor() >= 280:
        ball.wall_bounce()
    # the bottom
    if ball.ycor() <= -280 :
        ball.wall_bounce()

screen.exitonclick()