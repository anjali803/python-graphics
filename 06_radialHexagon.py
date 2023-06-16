from turtle import Turtle
t= Turtle()
t.screen.bgcolor("blue")  #to change the screen color
def radialHexagon(t,n,length):
    for i in range(6):
        t.forward(length)
        t.right(360/n)
radialHexagon(t,6,100)