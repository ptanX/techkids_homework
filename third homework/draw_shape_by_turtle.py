from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape_numbers = len(colors)
edges_start = 3
current_shape = edges_start
step = 1
loops_range = int(shape_numbers*(2*edges_start+shape_numbers-1)/2)
for i in range(loops_range):
    color(colors[step-1])
    forward(100)
    left(360/current_shape)
    if (i == int(step*(2*edges_start+step-1)/2 -1)):
        step += 1
        current_shape += 1
