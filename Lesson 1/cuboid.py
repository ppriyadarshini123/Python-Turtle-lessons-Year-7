import turtle
import time
turtle.Screen().bgcolor("blue")

#myTurtle= turtle.Turtle()

#myTurtle.goto(10,10)
#myTurtle.goto(100,100)
#Extension: change turtle shape, change turtle size
#change turtle shape: "turtle","arrow","circle","square","arrow","mrBiangle","classic"
#myTurtle.shape("classic")
#myTurtle.shapesize(10,10,10)
#myTurtle.fillcolor("yellow")#fille colour
#myTurtle.pencolor("green")#outline colour



myTurtle2= turtle.Turtle()
myTurtle2.speed(1)
#Front square
myTurtle2.goto(0,0)  
myTurtle2.goto(0,100)
myTurtle2.goto(100,100)
myTurtle2.goto(100,0)
myTurtle2.goto(0,0)

#Back square
myTurtle2.goto(20,20) # Bottom left line
myTurtle2.goto(120,20)
myTurtle2.goto(120,120)
myTurtle2.goto(20,120)
myTurtle2.goto(20,20)

#top left line
myTurtle2.penup()
myTurtle2.goto(0,100)
myTurtle2.pendown()
myTurtle2.goto(20,120)

#Bottom right line
myTurtle2.penup()
myTurtle2.goto(100,0)
myTurtle2.pendown()
myTurtle2.goto(120,20)

#Top right line
myTurtle2.penup()
myTurtle2.goto(100,100)
myTurtle2.pendown()
myTurtle2.goto(120,120)


time.sleep(5)

