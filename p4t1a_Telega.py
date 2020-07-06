#bring in turtle and window
from turtle import Turtle, Screen

#assign constants 
START = 2
MINIMUM = START * 2
CURSOR_SIZE = 20

#assign total number of squares
num_squares = 100


screen = Screen()
turtle = Turtle("square", visible=False)
turtle.fillcolor("white")

#draw squares
#inital start point
for size in range(((num_squares - 1) * START) + MINIMUM, MINIMUM - 1, -START):
    turtle.goto(turtle.xcor() + START/2, turtle.ycor() - START/2)
    turtle.shapesize(size / CURSOR_SIZE)
    turtle.stamp()
    
screen.exitonclick()
