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

# move turtle to cenmrBe of screen 

mrB.goto(0,0) 

# use turtle commands to create a Square below 
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
  

# use turtle commands to draw a Rectangle below 
# move turtle to cenmrBe of screen
mrB.goto(-50,-50)
mrB.fillcolor("red")
mrB.begin_fill()

mrB.forward(100)
mrB.left(90)
mrB.forward(50)
mrB.left(90)
mrB.forward(100)
mrB.left(90)
mrB.forward(50)
mrB.left(90)
mrB.end_fill()
  

# Extension - draw a 3-D cuboid below 

mrB.clear() 
  
# Forming the window screen 
tut = turtle.Screen() 



# background color green 
tut.bgcolor("green") 
  
# window title Turtle 
tut.title("Turtle") 
my_pen = turtle.Turtle() 

#my_pen.fillcolor("red")
#my_pen.begin_fill()
# object color 
my_pen.color("orange") 
tut=turtle.Screen()            
  
# forming front rectangle face 
my_pen.forward(100) 
my_pen.left(90) 
my_pen.forward(150) 
my_pen.left(90) 

my_pen.forward(100) 
my_pen.left(90) 
my_pen.forward(150) 
my_pen.left(90) 
  
# bottom left side 
my_pen.goto(50,50) 
  
# forming back rectangle face 
my_pen.forward(100) 
my_pen.left(90) 
my_pen.forward(150) 
my_pen.left(90) 

my_pen.forward(100) 
my_pen.left(90) 
my_pen.forward(150) 
my_pen.left(90) 
  
# bottom right side 
my_pen.goto(150,50) 
my_pen.goto(100,0) 
  
# top right side 
my_pen.goto(100,150) 
my_pen.goto(150,200) 
  
# top left side 
my_pen.goto(50,200) 
my_pen.goto(0,150)
#my_pen.end_fill()

time.sleep(5)

 