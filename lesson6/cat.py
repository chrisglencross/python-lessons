import turtle

turtle.register_shape("cat.gif")
cat=turtle.Turtle("cat.gif")
cat.speed("fastest")

def cat_released(x, y):
    cat.goto(x, y)
    cat.fillcolor("red")
    cat.begin_fill()
    for i in range(0, 45):
        cat.left(8)
        cat.forward(1)
    cat.end_fill()

cat.onrelease(cat_released)
