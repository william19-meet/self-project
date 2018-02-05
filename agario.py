import turtle
import math
import time
##import pygame.base
import random
from Ball import Ball


RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 7

global score

####pygame.init()
####
####pygame.mixer.music.load("music.wav")
####
####pygame.mixer.music.play(-1)
####pygame.mixer.music.set_volume(0.3)

score_list = []





score = 0


MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

turtle.tracer(0)
turtle.hideturtle()

MY_BALL = Ball(0,0,5,5,15,"red")




for I in range(NUMBER_OF_BALLS):
    x = random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    y = random.randint(round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
    dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    while dx == 0 or dy == 0:
        dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    color = (random.random(), random.random(), random.random())

    RANDOM_BALLS = Ball(x,y,dx,dy,radius,color)

    BALLS.append(RANDOM_BALLS)




def move_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)



def collide(ball_a,ball_b):
    if ball_a == ball_b:
        return False
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d + 10 <= ball_a.r + ball_b.r:
        return True
    else:
        return False


def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a, ball_b):
                x = random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
                y = random.randint(round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
                dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                while dx == 0 or dy == 0:
                    dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                color = (random.random(), random.random(), random.random())
                if ball_a.r  > ball_b.r:
                    ball_b.goto(x, y)
                    ball_b.r = radius
                    ball_b.dx = dx
                    ball_b.dy = dy
                    ball_b.color(color)
                    ball_b.shapesize(ball_b.r/10)
                    ball_a.r = ball_a.r+1
                    ball_a.shapesize(ball_a.r/10)
                else:
                    ball_a.r = radius
                    ball_a.goto(x, y)
                    ball_a.dx = dx
                    ball_a.dy = dy
                    ball_a.color(color)
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.r = ball_b.r+1
                    ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball):
            global score
            if MY_BALL.r < ball.r:
                turtle.goto(-160,0)
                turtle.write('GAME OVER',move=True, align="left", font=("Arial", 40, "normal"))
                return False



            x = random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
            y = random.randint(round(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
            dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            while dx == 0 or dy == 0:
                dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
            radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
            color = (random.random(), random.random(), random.random())
            if MY_BALL.r > ball.r:
                ball.goto(x,y)
                ball.r = radius
                ball.x = x
                ball.y = y
                ball.dx = dx
                ball.dy = dy
                ball.color(color)
                ball.shapesize(ball.r/10)
                MY_BALL.r += 1
                MY_BALL.shapesize(MY_BALL.r/10)
                turtle.clear()
                score = score + 1
                turtle.goto(-SCREEN_WIDTH/2-165, SCREEN_HEIGHT/2+120)
                turtle.write('score = ' + str(score),move=False, align="left", font=("Arial", 14, "normal"))

    return True 	

def movearound(event):
	X = event.x - round(SCREEN_WIDTH)
	Y = round(SCREEN_HEIGHT) - event.y
	MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>" , movearound)
turtle.getscreen().listen()

while RUNNING:
    if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
        SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

    move_balls()
####################    MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    check_all_balls_collision()
    RUNNING=check_myball_collision()
    turtle.getscreen().update()
    time.sleep(SLEEP)

turtle.mainloop()
                

                            
























