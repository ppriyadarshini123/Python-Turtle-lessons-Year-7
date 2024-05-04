import turtle

#Spirals tutorial:https://holypython.com/turtle-spirals/?utm_content=cmp-true
#https://www.101computing.net/turtle-spiral/
#https://www.101computing.net/python-iteration/
#create your turtle, give it your name
mrB = turtle.Turtle()

# set colour of the Pen that the turtle will use
mrB.pencolor("red")
# set pen thickness
mrB.pensize(5)

# move and turn your turtle
mrB.forward(100)
mrB.left(90)
mrB.forward(100)

mrB.clear()

# your turn to do the stuff ;-)
for i in range(100):
    mrB.forward(5+i)
    mrB.right(35)



mrB.clear()

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
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

