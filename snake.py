from turtle import Turtle


class Snake:
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Snake.STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append((new_segment))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(Snake.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

    def left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)