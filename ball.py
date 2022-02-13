from turtle import Turtle
import random

INITIAL_DIRECTION = [0,30,60,120,150,180,210,240]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed('fast')
        self.penup()
        self.setheading(random.choice(INITIAL_DIRECTION))
        
    def ball_move(self):
        self.forward(20)
    
    def wall_bounce(self):
        old_head = self.heading()
        new_head = - old_head
        self.seth(new_head)
