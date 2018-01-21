import turtle
import time
import random
from Ball import Ball


RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

BALLS = []

MY_BALL = Ball(0,0,10,10,5,"red")




for I in range(NUMBER_OF_BALLS):
    x = random.randit(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    y = random.randit(round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
    dx = random.randit(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy = random.randit(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randit(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    color = (random.randit(), random.randit(), random.randit())

    RANDOM_BALLS = Ball(x,y,dx,dy,radius,color)

    BALLS.append(RANDOM_BALLS)




def move_balls(SCREEN_WIDTH,SCREEN_HEIGHT,BALLS):
    for ball in BALLS:
        ball.penup()
        random_x_pos = random.randint(round(-SCREEN_WIDTH + RADIUS), round(SCREEN_WIDTH-RADIUS))
        random_y_pos = random.randint(round(-SCREEN_WIDTH + RADIUS), round(SCREEN_HEIGHT - RADIUS))
        ball.goto(random_x_pos,random_y_pos)

    
    

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5



turtle.tracer(1,0)
turtle.hideturtle()
