import turtle
import time
turtle.Screen().bgcolor("blue")

myTurtle= turtle.Turtle()

myTurtle.goto(10,10)
#myTurtle.goto(100,100)
#Extension: change turtle shape, change turtle size
#change turtle shape: "turtle","arrow","circle","square","arrow","triangle","classic"
myTurtle.shape("classic")
myTurtle.shapesize(10,10,10)
myTurtle.fillcolor("yellow")#fille colour
myTurtle.pencolor("green")#outline colour
time.sleep(5)
