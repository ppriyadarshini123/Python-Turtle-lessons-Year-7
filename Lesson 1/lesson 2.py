"""
The code below is to get you started - do not delete anything without checking first with your teacher
"""
import turtle
import time
#create your turtle, give it your name by replacing mrB with your name at all the places below
# set background colour
turtle.Screen().bgcolor("blue")
# setup your Turtle
mrB = turtle.Turtle()
#Change turtle speed
mrB.speed(1)

# move turtle to cenmrBe of screen
mrB.goto(0,0)
mrB.fillcolor("pink")
mrB.begin_fill()

mrB.forward(100)
mrB.left(90)
mrB.forward(100)
mrB.left(90)
mrB.forward(100)
mrB.left(90)
mrB.forward(100)
mrB.left(90)
mrB.end_fill()



# use turtle commands to move the turtle below

mrB.speed(5)
# use turtle commands to draw a square below
mrB.fillcolor("yellow")
mrB.begin_fill()
mrB.right(90)
mrB.forward(100)
mrB.left(90)
mrB.forward(100)
mrB.left(90)
mrB.forward(100)
mrB.end_fill()

# Extension - find out how to create another turtle and move it around the screen as well
# change turtle speed



mrsP = turtle.Turtle()
mrsP.speed(10)

# move turtle to cenmrBe of screen
mrsP.goto(-50,-50)
mrsP.fillcolor("purple")
mrsP.begin_fill()
mrsP.forward(100)
mrsP.left(90)
mrsP.forward(100)
mrsP.left(90)
mrsP.forward(100)
mrsP.left(90)
mrsP.forward(100)
mrsP.left(90)
mrsP.end_fill()




time.sleep(10)
