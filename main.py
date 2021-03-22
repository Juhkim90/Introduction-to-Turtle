'''
# Introduction to the Turtle

1. Import the Turtle library (Top of the code)
import turtle

2. Create a pen / turtle
variable1 = turtle.Turtle()

3. Create a paper / screen
variable2 = turtle.Screen()

4. Movements

	a) forward
	variable1.forward(DISTANCE)
	variable1.fd(DISTANCE)

	b) backward
	variable1.backward(DISTANCE)
	variable1.bk(DISTANCE)

	c) turn right
	variable1.right(ANGLE)

	d) turn left
	variable1.left(ANGLE)

	e) pen up
	variable1.penup()

	f) pen down
	variable1.pendown()

	g) go to a specific point
	variable1.goto(X,Y)

	h) go to home (origin)
	variable1.home()

'''
import turtle
pen=turtle.Turtle()
paper=turtle.Screen()

pen.forward(100)
pen.backward(10)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(120)
pen.penup()
pen.goto(40,0)
pen.pendown()
pen.backward(40)
pen.left(90)
pen.forward(20)
pen.right(90)
pen.forward(40)

# Draw a Window
# Draw a House

# Draw a favorite letter (Homework or Review)

'''
5. Change turtle speed
variable1.speed(SPEEDS)
*NOTE: SPEEDS from 1 to 10

6. Change width of line
variable1.width(WIDTH)
variable1.pensize(WIDTH)
*NOTE: WIDTH from 0 to 10

7. Change color of pen
variable1.color(COLOR)
*NOTE: COLOR is in STRING 
'''
# Draw a favorite letter (Homework or Review)


import turtle
pen = turtle.Turtle()
pen.speed(10)
index = 0
length = 10
penColor = ["red","orange","yellow","green","blue","navy","purple"]
while(True):
	pen.color(penColor[index])
	pen.left(70)
	pen.forward(length)
	index += 1
	length += 0.5
	if (index == len(penColor)):
		index = 0


'''
8. Change shape of pen
variable1.shape(SHAPE)
*NOTE: SHAPE is in STRING
SHAPE: arrow, turtle, circle, square, triangle, classic

9. Write text
variable1.write(TEXT)
*NOTE: TEXT is in STRING

10. Fill color
variable1.begin_fill()
# Draw a Shape that wanted to be colored
variable1.end_fill()

11. Draw circle
variable1.circle(RADIUS)
variable1.circle(RADIUS, ANGLE)
variable1.circle(RADIUS, ANGLE, Side)
'''

# Draw a card

import turtle

sharpie = turtle.Turtle()
sharpie.color("lightblue")
sharpie.width(3)

sharpie.fillcolor("yellow")

board = turtle.Screen()
board.bgcolor("black")

sharpie.begin_fill()

#DRAW a pentagon
sharpie.forward(100)
sharpie.left(360/5)
sharpie.forward(100)
sharpie.left(360/5)
sharpie.forward(100)
sharpie.left(360/5)
sharpie.forward(100)
sharpie.left(360/5)
sharpie.forward(100)
sharpie.left(360/5)

sharpie.end_fill()



sharpie.circle(50) # Full Circle in radius 50
sharpie.circle(100, 180) # Semi Circle in radius 100
sharpie.circle(100, 180, 5) # Half of a Pentagon