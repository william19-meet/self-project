from turtle import Turtle
turtle.penup()
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
        
        
    
        
    
turtle.goto(x,y)

turtle.mainloop()
