import turtle
import time
s=turtle.getscreen()
t=turtle.Turtle()

#Change the title of the screen
turtle.title("My Turtle program")

#Changing the size and color of the pen
t.pensize(2)
t.pencolor("green")

t.shape("turtle") #arrow, circle

#Change the speed of the turtle
t.speed(5)

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

t.goto(100,100)

t.home()

t.clear()
t.pen(pencolor="purple",fillcolor="orange",pensize=4,speed=9)
t.speed(1) # Any number ranging from 0(slowest speed) to 10(highest speed)
t.begin_fill() 
t.fillcolor("red")
t.stamp()
t.circle(50)
t.stamp()
t.end_fill()
t.clearstamp(1)

t.penup()
t.goto(40,40)
t.pendown()

#Draws a dot of radius 20
t.dot(20)

#Cloning the turtle
c=t.clone()
t.color("yellow")
c.color("green")
t.circle(100)
c.circle(60)

#Change the turtle size
#t.shapesize(1,5,5) # stretch length=1, stretch width=5, outline width=10
#t.shapesize(10,5,1)

#Using for loop
for i in range(4):
    t.forward(100)
    t.right(90)


#Using while loop
n=10
t.pencolor("blue")
while n<=40:
    t.circle(n)
    n=n+20

u=input("Would you like me to draw a shape? Type yes or no:")
if u=="yes":
    t.pencolor("purple")
    t.circle(50)
elif u=="no":
    print("okay")
else:
    print ("Invalid reply")

time.sleep(10)