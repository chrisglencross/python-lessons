import turtle

def draw_square(size):
    for side in range(0, 4):
        turtle.forward(size)
        turtle.right(90)

size=5
for square in range(0, 100):
    draw_square(size)
    size=size+5
    turtle.right(10)
            
