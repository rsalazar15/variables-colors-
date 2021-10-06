#Initialize
import turtle
import random
t=turtle.Turtle() 
turtle.colormode(255)
#Functions
def randomDot():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(20,100)
    t.color(r,g,b)
    t.begin_fill()
    t.circle(c)
    t.end_fill()
#Main
randomDot() 



