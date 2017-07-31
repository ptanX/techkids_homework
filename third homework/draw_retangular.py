from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    for j in range(4):
        if j%2 == 0:
            forward(50)
            left(90)
        else:
            forward(100)
            left(90)
    end_fill()
    forward(50)
