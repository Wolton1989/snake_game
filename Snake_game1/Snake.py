from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = RIGHT

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(self.direction)
        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction):
        self.direction = direction

    def up(self):
        if self.direction != DOWN:
            self.set_direction(UP)

    def down(self):
        if self.direction != UP:
            self.set_direction(DOWN)

    def left(self):
        if self.direction != RIGHT:
            self.set_direction(LEFT)

    def right(self):
        if self.direction != LEFT:
            self.set_direction(RIGHT)
