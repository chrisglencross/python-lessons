import turtle

# Which bit of the Mandelbrot set do we want to draw?
centre_x=-0.7
centre_y=0.0
scale=3.076
max_iterations=100

# How big do we want the image?
image_width=200
image_height=200
pensize=5

# The Mandelbrot function
def calculate_iterations(x0, y0):
    i=0
    x=x0
    y=y0
    while i<max_iterations and x*x+y*y<4:
        next_x = x*x - y*y + x0
        y = 2*x*y + y0
        x = next_x
        i = i+1
    return i

# Creates a list of which colour to use for each iteration
def create_colour_palette():
    colours=[]
    for i in range(0, max_iterations):
        red=(2*i/max_iterations+0.5)%1.0
        green=(i*3/max_iterations)%1.0
        blue=(i*5/max_iterations+0.2)%1.0
        colours.append( (red, green, blue) )
    colours.append( (0, 0, 0) )
    return colours

colours=create_colour_palette()

start_x=centre_x-scale/2
inc_x=scale/image_width

start_y=centre_y-scale/2
inc_y=scale/image_height

turtle.speed("fastest")
turtle.hideturtle()
turtle.pensize(pensize)

y=start_y
for py in range(0, image_height):

    # Go to start of the line
    turtle.penup()
    turtle.goto((0-image_width/2)*pensize, (0-image_height/2+py)*pensize)
    turtle.pendown()

    # See how many pixels in a row are the same colour, and draw a line
    x=start_x
    prev_iterations=calculate_iterations(x, y)
    for px in range(1, image_width):
        iterations=calculate_iterations(x, y)
        if prev_iterations != iterations or px == image_width-1:
            colour=colours[prev_iterations]
            turtle.color(colour)
            turtle.goto((0-image_width/2+px)*pensize, (0-image_height/2+py)*pensize)
            prev_iterations = iterations
        x=x+inc_x
        
    y=y+inc_y
        
