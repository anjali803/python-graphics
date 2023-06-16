from turtle import Turtle
t = Turtle()
t.speed(1)
def drawHexagon(t,length):
    for count in range(6):
        t.forward(length)
        t.right(60)
drawHexagon(t,100)

