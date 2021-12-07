from turtle import Turtle

PADDLE_COLOR = "white"

class Paddle(Turtle):
        def __init__(self, x_cor, y_cor):
                super().__init__()     
                self.x_cor = x_cor #X-coord of any paddle
                self.y_cor = y_cor #Y-coord of any paddle
                self.createPaddle()
        
        #Method to construct new paddle
        def createPaddle(self):
                self.shape('square')
                self.color(PADDLE_COLOR)
                self.penup()
                self.home()
                self.shapesize(stretch_wid=5, stretch_len=1)
                self.goto(self.x_cor,self.y_cor)

        #Method for the upward motion of the paddle
        def go_up(self):
                new_y = self.ycor() + 30 #Move the paddle by 30 pixels upward
                self.goto(self.xcor(), new_y)

        #Method for the downward motion of the paddle
        def go_down(self):
                new_y = self.ycor() - 30 #Move the paddle by 30 pixels downward
                self.goto(self.xcor(), new_y)