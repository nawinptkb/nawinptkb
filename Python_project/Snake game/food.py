from turtle import Turtle
import random as r


class Food(Turtle):
        #Create the food
        def __init__(self):
                super().__init__()
                self.shape('circle')
                self.penup()
                self.shapesize(stretch_len=0.5 , stretch_wid=0.5) #Now the food will be 10x10 pixels in dimension
                self.color('red')
                self.speed('fastest') #Speed of how the food is generated
                self.refresh_food() #Execute the method refresh_food to random the location of the snake's food 

        def refresh_food(self):
                random_x = r.randint(-280,280) #Since the dimension of the screen is x = 600 
                random_y = r.randint(-280,280) #and y = 600 the food should be randomized with in the edge
                self.goto(random_x,random_y) #Set the location of the food
                

        