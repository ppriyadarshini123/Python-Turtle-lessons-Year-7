"""
The code below is to get you started - do not delete anything without checking first with your teacher
"""
import turtle
import time
#create your turtle, give it your name by replacing mrB with your name at all the places below
# set background colour
turtle.Screen().bgcolor("yellow")
# setup your Turtle
mrB = turtle.Turtle()
# move turtle to cenmrBe of screen
mrB.goto(0,0)
# Task 1: using the space below, use turtle commands to draw a Star
# executing loop 5 times for a star
for i in range(5): 
        # moving turtle 100 units forward
        mrB.forward(100)
 
        # rotating turtle 144 degree right
        mrB.right(144)

mrB.clear()
# Task 2: using the space below, use turtle commands to draw a nested Square (square within a square) or a nested Circle (circle within a circle)

mrB.right(90)
x=0
y=100
for j in range(2):
        for i in range(4):
                mrB.forward(y)
                mrB.left(90)
        mrB.penup()
        x=x+10
        y=y-40
        mrB.goto(x+10,-(x+10))
        mrB.pendown()

mrB.clear()

# Extension - Find out what the Olympic Rings look like - use the space below to create these with the correct colours
# set thickness for each ring
turtle.Screen().bgcolor("white")
mrB.pensize(5)
 
mrB.color("blue")
mrB.penup()
mrB.goto(-110, -25)
mrB.pendown()
mrB.circle(45)
 
mrB.color("black")
mrB.penup()
mrB.goto(0, -25)
mrB.pendown()
mrB.circle(45)
 
mrB.color("red")
mrB.penup()
mrB.goto(110, -25)
mrB.pendown()
mrB.circle(45)
 
mrB.color("yellow")
mrB.penup()
mrB.goto(-55, -75)
mrB.pendown()
mrB.circle(45)
 
mrB.color("green")
mrB.penup()
mrB.goto(55, -75)
mrB.pendown()
mrB.circle(45)


time.sleep(5)