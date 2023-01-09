from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0
START_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)


    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_num-1].xcor()
                new_y=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            
    def add_segment(self,position):
            seg=Turtle(shape="square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def extend(self):
        #add a new segment 
        self.add_segment(self.segments[-1].position())