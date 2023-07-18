from turtle import Turtle
import random 

def radialPatternWtihRandomColor(t,x,y,shape,color):
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.setheading(0)
    t.down()
    t.shape(shape)
    t.fillcolor(color)
    t.end_fill()
t=Turtle()
t.speed(1)
radialPatternWtihRandomColor(t,30,30,"square","yellow")