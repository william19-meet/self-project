import turtle
from turtle import *

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self, shape = 'circle')
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = y
        self.r = r
        self.shapesize = self.r/10
        self.color(color)

        turtle.penup()
        turtle.goto(x,y)

        
    def move(self,screen_width,screen_height):
        current_x = self.x
        newx = current_x - self.dx
        
        current_y = self.x
        newy = current_y - self.dy
        
        top = height/2
        bottom = -(height/2)
        right = width/2
        left = -(width/2)
        
        rightside = newx + self.r
        leftside = newx - self.r
        upside = newy + self.r
        bottomside = newy - self.r


        if right_side_ball >= screen_width/2:
            newx = current_x

        if left_side_ball <= screen_width/-2:
            newx = current_x

        if top_side_ball >= screen_height/2:
            newy = current_y

        if bottom_side_ball <= screen_height/-2:   
            newy = current_y

        
    
        turtle.goto(x,y)

turtle.mainloop()
