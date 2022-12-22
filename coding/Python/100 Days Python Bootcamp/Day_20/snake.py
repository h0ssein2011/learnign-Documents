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
        self.segment = []
        self.create_segment()
        self.head = self.segment[0]
       
       

    def create_segment(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.color(self.color)
            new_turtle.shape(self.shape)
            new_turtle.penup()
            new_turtle.setposition(i*-10,0)
            self.segment.append(new_turtle)
    

    def move(self):
            for loc in range(len(self.segment) -1 ,0,-1):
                new_x = self.segment[loc-1].xcor() 
                new_y = self.segment[loc-1].ycor() 
                self.segment[loc].goto(new_x,new_y)
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
      

        


