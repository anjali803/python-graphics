# draw a square------
from turtle import Turtle
import time
t = Turtle()
# time.sleep(5)
t.speed(3)
def drawSquare(t,x,y,length):
    t.fillcolor("red")
    t.pencolor("blue")
    
    t.goto(x,y)
    # t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
drawSquare(t,0,0,100)





# from turtle import Turtle
# t = Turtle()
# def drawsquare(t,x,y,length):
#     t.goto(x,y)
#     t.setheading(270)
#     for count in range(4):
#         t.forward(length)
#         t.left(90)
# drawsquare(t,0,0,100)