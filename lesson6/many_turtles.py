import turtle

def draw_circle(the_turtle, size):
    for side in range(0, 180):
        the_turtle.forward(size)
        the_turtle.left(2)

green_turtle=turtle.Turtle(shape="turtle")
green_turtle.color("green")
green_turtle.shapesize(10)
green_turtle.pensize(3)

red_arrow=turtle.Turtle(shape="arrow")
red_arrow.color("red")
red_arrow.shapesize(5)
red_arrow.pensize(5)

draw_circle(green_turtle, 10)
draw_circle(red_arrow, 5)
