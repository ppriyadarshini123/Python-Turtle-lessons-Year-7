import turtle
import time
#create your mrB, give it your name
mrB = turtle.Turtle()

screen = turtle.Screen().bgcolor("yellow")
# set colour of the Pen that the mrB will use
mrB.pencolor("red")
# set pen thickness
mrB.pensize(5)
blade_length=95

# move and turn your mrB
mrB.forward(100)
mrB.left(90)
mrB.forward(100)

mrB.clear()

# your turn to do stuff ;-)
#Fan

for i in range(3):
    mrB.penup()
    mrB.backward(blade_length)
    mrB.fillcolor("green")
    mrB.begin_fill()
    mrB.pendown()
    mrB.forward(2*blade_length)
    mrB.left(120)
    mrB.circle((1/3)*blade_length*(3**(1/2)),120)
    mrB.circle(-(1/3)*blade_length*(3**(1/2)),120)
    mrB.end_fill()
    mrB.right(120)
    mrB.penup()
    mrB.forward(blade_length)
    mrB.right(60)
    mrB.pendown()


mrB.clear()

#Cross
turtle.speed(0)
turtle.hideturtle()
turtle.color('red')

turtle.up()
turtle.goto(-150,0)
turtle.down()
turtle.begin_fill()
for _ in range(4):
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)      
turtle.end_fill()

time.sleep(15)
