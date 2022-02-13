from turtle import Turtle
import random

BALL_AXIS_SPEED = 15

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed('fast')
        self.penup()
        self.x_move = BALL_AXIS_SPEED
        self.y_move = BALL_AXIS_SPEED
        self.move_delay = 0.1
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1
        self.move_delay *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1
        self.move_delay = 0.1
