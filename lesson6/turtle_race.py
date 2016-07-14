import turtle

turtle.title("Turtle Race")
turtle1=turtle.Turtle(shape="turtle")
turtle2=turtle.Turtle(shape="turtle")

def win(the_turtle):
    "Spin the turtle when it wins"
    for i in range(0, 180):
        the_turtle.left(4)    

def turtle1_clicked(x, y):
    turtle1.forward(10)
    if turtle1.xcor() >= 200:
        win(turtle1)
        reset_turtles()

def turtle2_clicked(x, y):
    turtle2.forward(10)
    if turtle2.xcor() >= 200:
        win(turtle2)
        reset_turtles()

def reset_turtles():
    turtle1.reset()
    turtle1.color("red")
    turtle1.shapesize(5)
    turtle1.penup()
    turtle1.goto(-200, 100)
    turtle1.pendown()
    turtle1.onclick(turtle1_clicked)
    turtle2.reset()
    turtle2.color("green")
    turtle2.shapesize(5)
    turtle2.penup()
    turtle2.goto(-200, -100)
    turtle2.pendown()
    turtle2.onclick(turtle2_clicked)

reset_turtles()

