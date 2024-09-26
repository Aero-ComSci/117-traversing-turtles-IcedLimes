import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)
    t.penup()

startx = 0
starty = 0
direction = 90
more_move=0

for t in my_turtles:
    t.goto(startx, starty)
    new_color = turtle_colors.pop()
    t.color(new_color)
    t.setheading(direction+85)
    t.pendown()
    t.forward(25+more_move)
    startx = t.xcor()
    starty = t.ycor()
    direction = t.heading()-15
    more_move = more_move+15

wn = trtl.Screen()
wn.mainloop()
