import turtle
from turtle import *

turtle.hideturtle()
turtle.penup()

##border = turtle.clone()
##border.penup()
##border.goto(400/2,-400/2)
##border.pendown()
##border.goto(400/2,400/2)
##border.goto(-400/2,400/2)
##border.goto(-400/2,-400/2)
##border.goto(400/2,-400/2)
##border.hideturtle()



class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self, shape = 'circle')
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shapesize(self.r/10)
        self.color(color)
        
    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        newx = current_x + self.dx
##        self.x = newx
##        print("x:"+str(self.xcor()), "y:"+str(self.ycor()))
        current_y = self.ycor()
        newy = current_y + self.dy
##        self.y=newy
        self.goto(newx,newy)

##        top = screen_height
##        bottom = -(screen_height/2)
##        right = screen_width/2
##        left = -(screen_width/2)
        
        right_side = newx + self.r
        left_side = newx - self.r
        top_side = newy + self.r
        bottom_side = newy - self.r
    

        if right_side >= screen_width:
            self.dx = -(self.dx)
            self.clear()

        if left_side <= -screen_width:
            self.dx = -(self.dx)
            self.clear()

        if top_side >= screen_height:
            self.dy = -(self.dy)
            self.clear()
        if bottom_side <= -screen_height:   
            self.dy = -(self.dy)
            self.clear()


##ball = Ball(0,0,10,1,20,"green")
##while True:
##    ball.move(400,400)
