import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('Green')

# Tell screen to not show automatically
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(3)

# Hide the turtle, we only want to see the drawing
t.hideturtle()

def draw_circle():
    t.fillcolor("Orange")
    t.begin_fill()
    t.circle(50)  # Adjust the radius as desired
    t.end_fill()

t.penup()
t.goto(-350, 0)
t.pendown()

while True:
    t.clear()
    draw_circle()

    # Only now show the screen as one of the frames
    screen.update()
    t.forward(0.02)
