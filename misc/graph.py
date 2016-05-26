import turtle
import math

def fn(x):
    # return x*x
    return math.sin(math.radians(x))

# Calculate x and y points on graph
xs = list(range(0, 721, 1))
ys = list(map(fn, xs))

# Calculate min and maximum points on graph
min_x = min(xs)
min_y = min(ys)
max_x = max(xs)
max_y = max(ys)
print(min_x, min_y, max_x, max_y)

# Scale the graph so it appears centrally
graph_size = 1000
scale_x = graph_size / (max_x-min_x)
scale_y = graph_size / (max_y-min_y)
offset_x = scale_x * ((max_x+min_x)/2);
offset_y = scale_y * ((max_y+min_y)/2);
print(scale_x, scale_y)
print(offset_x, offset_y)

# Draw graph axis
turtle.penup()
turtle.goto(min_x*scale_x-offset_x, 0-offset_y)
turtle.pendown()
turtle.goto(max_x*scale_x-offset_x, 0-offset_y)
turtle.penup()
turtle.goto(0-offset_x, min_y*scale_y-offset_y)
turtle.pendown()
turtle.goto(0-offset_x, max_y*scale_y-offset_y)
turtle.penup()

turtle.goto(xs[0] * scale_x - offset_x, ys[0] * scale_y - offset_y)
turtle.pencolor("red")
turtle.pendown()
for x, y in zip(xs, ys):
    turtle.goto(x * scale_x - offset_x, y * scale_y - offset_y)


