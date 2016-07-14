import turtle

turtle.reset()
turtle.width(50)

for line in range(0,10):
    
    turtle.penup()
    turtle.goto(-500, line*50-250)
    turtle.pendown()

    turtle.color(((10-line)/10, line/10, line/10))
    turtle.forward(1000)
