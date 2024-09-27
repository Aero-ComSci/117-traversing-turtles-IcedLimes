import turtle as trtl

class Manager:
    def __init__(self, shapes, colors):
        self.my_turtles = []  # create an empty list of turtles
        self.turtle_shapes = shapes  # list of turtle shapes
        self.turtle_colors = colors  # list of turtle colors

# creates a turtle for every shape in shapes
        for shape in self.turtle_shapes:
            t = trtl.Turtle(shape)
            t.speed(0)
            t.penup()
            self.my_turtles.append(t)

    def move_turtles(self):
        # creates starting point for turtle
        startx = 0
        starty = 0
        # creates the set heading direction
        direction = 90
        # used to add more distance so it can spiral outwards
        more_move = 0

# runs loop for however many things there are in my_turtles 
        for i in range(len(self.my_turtles)):
            # turtle changes into next value in my_turtles every loop
            t = self.my_turtles[i]
            # goes to starting position
            t.goto(startx, starty)
            # becomes next value in turtle_colors every loop
            t.color(self.turtle_colors[i])
            # changes direction by 70 degrees
            t.setheading(direction + 70)
            t.pendown()
            # moves forward 25 added with more_move
            t.forward(25 + more_move)
            # changes starting position to the position its in after it moves
            startx = t.xcor()
            starty = t.ycor()
            # direction becomes current direction to it can add 70 again for the next loop to spiral outwards
            direction = t.heading()
            # gives extra distance to it can spiral instead of being a circle
            more_move += 15

    def __str__(self):
        turtle_info = ""
        for t in self.my_turtles:
            turtle_info += "shape: {}, color: {}\n".format(t.shape(), t.color()[0])
        return turtle_info

# Use interesting shapes and colors
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]

colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

turtle_manager = Manager(shapes, colors)

turtle_manager.move_turtles()

print(turtle_manager)

wn = trtl.Screen()
wn.mainloop()
