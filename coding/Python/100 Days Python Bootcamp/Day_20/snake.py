from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self,color='white',shape='square'):
        self.color = color
        self.shape = shape
        self.segments = []
        self.create_segment()
        self.head = self.segments[0]
       
       

    def create_segment(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
 
    
    def add_segment(self,position):
            new_turtle = Turtle()
            new_turtle.color(self.color)
            new_turtle.shape(self.shape)
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    

    def move(self):
            for loc in range(len(self.segments) -1 ,0,-1):
                new_x = self.segments[loc-1].xcor() 
                new_y = self.segments[loc-1].ycor() 
                self.segments[loc].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
      

        


