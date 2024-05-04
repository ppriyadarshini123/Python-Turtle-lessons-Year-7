import turtle

#Spirals tutorial:https://holypython.com/turtle-spirals/?utm_content=cmp-true
#https://www.101computing.net/turtle-spiral/
#create your turtle, give it your name
mrB = turtle.Turtle()

#mrB = turtle.Turtle()
mrB.speed(0)
mrB.color("#FF0000")

side=400
mrB.penup()
mrB.goto(-200,-200) #position cursor at the bootom right of the screen
mrB.pendown()

#Start Spiral
for i in range (1,100):
   mrB.forward(side)
   mrB.left(90)
   side=side-4

mrB.clear()
#
import os

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

def demo_one():
	
	# setup turtle pen
	t= turtle.Pen()
	
	# changes the speed of the turtle
	t.speed(10)
	
	# changes the background color
	turtle.bgcolor("black")
	
	# make spiral_web
	for x in range(200):
		t.pencolor(colors[x%6]) # setting color
		t.width(x/100 + 1) # setting width
		t.forward(x) # moving forward
		t.left(59) # moving left
	
	turtle.done()
	t.speed(10)
	
	turtle.bgcolor("black") # changes the background color
	
	# make spiral_web
	for x in range(200):
		t.pencolor(colors[x%6]) # setting color
		t.width(x/100 + 1) # setting width
		t.forward(x) # moving forward
		t.left(59) # moving left
	
	turtle.done()
	return
	
#end def

def demo_two():

	turtle.speed(0)
	
	turtle.pencolor('yellow')
	turtle.bgcolor('black')
	
	x=0
	
	turtle.penup()
	turtle.goto(0,50)
	turtle.pendown()
	
	while x < 60:
	    for i in range(6):
	        turtle.forward(100)
	        turtle.right(61)
	    turtle.right(11.11)
	    x=x+1
	#turtle.done()
	return turtle
	
#end def


# main

tname = demo_two()
go = input("Press enter to continue...")
os.system('clear')
tname.clear()

demo_one()
