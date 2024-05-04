"""
The code below is to get you started - do not delete anything without checking first with your teacher
"""
import turtle
#create your turtle, give it your name by replacing mrB with your name at all the places below
# set background colour
turtle.Screen().bgcolor("blue")
# setup your Turtle
mrB = turtle.Turtle()
# move turtle to cenmrBe of screen
mrB.goto(0,0)
# use turtle commands to create a Pentagon below

# taking input for the no of the sides of the polygon 
n = int(input("Enter the no of the sides of the polygon : ")) 
  
# taking input for the length of the sides of the polygon 
l = int(input("Enter the length of the sides of the polygon : ")) 
  
  
for i in range(n): 
    mrB.forward(l) 
    mrB.right(360 / n) 

mrB.clear()
# use turtle commands to draw a Hexagon below
#done as in penragon

# Extension#1 - draw a honeycomb below	

mrsP = turtle.Turtle()

for i in range(6):  
    mrsP.fillcolor("yellow")
    mrsP.begin_fill()  
    for comb in range(6):
        mrsP.forward(60)
        mrsP.right(60)
    mrsP.end_fill()

    
    mrsP.forward(60)
    mrsP.left(60)

# Extension#2 - fill in the shapes of the honeycomb with colour
#done