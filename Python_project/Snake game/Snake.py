from turtle import Turtle
#The snake body will be separated into 3 segments so we store 3 tuples in a list that will determine the coordinates of each part of the body segment
STARTING_POS = [(0,0), (-20,0), (-40,0)]

PACE = 20 #Travel distance of the snake

#Constants containing the angle which will determine the direction of the snake
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(object):
        def __init__(self):
            self.segments = [] #A list which will store each of the snake's body segment => in this case 3 segments
            self.create_snake() #Activating method create_snake to generate our snake everytime there is an instance of class snake created
            self.head = self.segments[0] #Head of the snake, which is actually stored in self.segments list at index 0 => coordinate (0,0)

        def create_snake(self):
                #For loop to create our snake's body 
                for position in STARTING_POS:
                        self.add_segment(position)
                        
        #Add segment to the snake's body to construct a whole snake 
        def add_segment(self, position):
                snake_segment = Turtle("circle") #Shape of the snake
                snake_segment.color("white") #Color of the snake
                snake_segment.penup()#Remove the trace of the turtle so that when the movement is activated the our snake do not leave any trace
                snake_segment.goto(position) #Set each segment to its position
                self.segments.append(snake_segment)#Store all segments into a list called segments
        """ => These are the same procedure as above for loop
                snake_segment_1 = Turtle("circle")
                snake_segment_1.color("white")
                snake_segment_1.goto(0,0)

                snake_segment_2 = Turtle("circle")
                snake_segment_2.color("white")
                snake_segment_2.goto(-20,0)

                snake_segment_3 = Turtle("circle") 
                snake_segment_3.color("white")
                snake_segment_3.goto(-40,0)
        """

        #add new segment to the snake after eating food
        def extend(self):
                self.add_segment(self.segments[-1].position()) #Add a new segment to same position as the last segment of the snake

        #reset the game after the snake collides with the wall; re-creating the snake again. The process is similar to the codes in __init__ part
        def reset_snake(self):
                for seg in self.segments:
                        seg.goto(1000,1000) #Remove the old snake from the display screen
                self.segments.clear() #Clear the list that stores snake's segments 
                self.create_snake() #Initialize the snake again at the center of the screen using the positions from the STARTING_POS list.
                self.head = self.segments[0] #Re-initialize the snake's head again so that the codes in game.py don't mess up.


        #Method for the movement of the snake
        def move(self):
                #For loop for the movement of the snake
                for seg_num in range(len(self.segments)-1 , 0, -1):
                        '''Get hold of the 2nd to last segment coordinates => The working is that we want the previous segment 
                        of the snake to be replace with the following segment so that the snake body could still connect to each other'''
                        new_x = self.segments[seg_num - 1].xcor()
                        new_y = self.segments[seg_num -1].ycor()
                        self.segments[seg_num].goto(new_x, new_y)
                self.head.forward(PACE) 

        #Each function outputs change the direction of the snake directing by the head => (snake's head)   
        def up(self):
                if self.head.heading() != DOWN:
                        self.head.setheading(UP)

        def left(self):
                if self.head.heading() != RIGHT:
                        self.head.setheading(LEFT)

        def down(self):
                if self.head.heading() != UP:
                        self.head.setheading(DOWN)

        def right(self):
                if self.head.heading() != LEFT:
                        self.head.setheading(RIGHT)


