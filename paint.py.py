import turtle
import random
bob = turtle.Turtle()
bob.color("red")
bob.pensize(5)
bob.speed(0)
def up():
    bob.setheading(90)
    bob.forward(100)
def down():
    bob.setheading(270)
    bob.forward(100)
def left():
    bob.setheading(180)
    bob.forward(100)
def right():
    bob.setheading(0)
    bob.forward(100)
turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.mainloop()
