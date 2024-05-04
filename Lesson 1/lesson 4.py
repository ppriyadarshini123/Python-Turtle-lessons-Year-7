"""
The code below is to get you started - do not delete anything without checking first with your teacher
"""
import turtle
import time

#create your turtle, give it your name by replacing mrB with your name at all the places below
# set background colour
turtle.Screen().bgcolor("light green")
# setup your Turtle
mrB = turtle.Turtle()
mrB.shape("turtle")
# move turtle to cenmrBe of screen
mrB.goto(0,0)
# use turtle commands to create a mrBiangle below

#First way
mrB.forward(100)
mrB.left(120)
mrB.forward(100)
mrB.left(120)
mrB.forward(100)
mrB.right(60)

mrB.clear()

#Second way
# taking input for the no of the sides of the polygon 
n = int(input("Enter the no of the sides of the polygon : ")) 
  
# taking input for the length of the sides of the polygon 
l = int(input("Enter the length of the sides of the polygon : ")) 
  
  
for i in range(n): 
    mrB.forward(l) 
    mrB.right(360 / n) 


mrB.clear()
# use turtle commands to draw a Circle below
mrB.fillcolor("red")
mrB.begin_fill()
mrB.circle(100)
mrB.end_fill()
mrB.clear()

# Extension - draw a 3-D pyramid below
mrsP = turtle.Turtle()
mrsP.pendown()
mrsP.speed(2)
mrsP.pensize(3)
mrsP.color("red")

#drawing the base of the square base pyramid
mrsP.forward(120)
mrsP.left(60)
mrsP.forward(50)
mrsP.left(120)
mrsP.forward(120)
mrsP.left(60)
mrsP.forward(50)
mrsP.left(120)

#top point of pyramid
mrsP.goto(70,150)
mrsP.goto(120,0)
mrsP.penup()
mrsP.left(60)
mrsP.forward(50)
mrsP.pendown()
#top point of pyramid
mrsP.goto(70,150)
mrsP.goto(30,50)





time.sleep(5)
