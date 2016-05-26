import turtle

def fern(size, pensize):

    if pensize < 1:
        return

    turtle.pensize(pensize)
    turtle.forward(size)
    
    turtle.right(55)
    fern(2*size/3, pensize-1)
    turtle.left(55)

    turtle.back(size/2)
    turtle.left(60)
    fern(size/2, pensize-1)
    turtle.right(60)

    turtle.back(size/2)


turtle.speed("fastest")
turtle.penup()
turtle.goto(-100, -400)
turtle.pendown()
turtle.left(80)
turtle.color("green")
fern(500.0, 10)
