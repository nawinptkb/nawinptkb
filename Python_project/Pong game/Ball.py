from turtle import Turtle


class Ball(Turtle):
        def __init__(self):
                super().__init__()
                self.shape('circle')
                self.color('red')
                self.shapesize(stretch_len=1 , stretch_wid=1)
                self.penup()
                self.home()
                
                self.x_move = 10
                self.y_move = 10

        #Method for the ball to move diagonally
        def move(self):
                new_x = self.xcor() + self.x_move
                new_y = self.ycor() + self.y_move
                self.goto(new_x, new_y)
        
        #Method for the ball to negate its y direction when hits the ball
        def bounce_y(self):
                self.y_move *= -1
        
        def bounce_x(self):
                self.x_move *= -1

        #Method for the ball to reset its position when the ball goes out of bound
        def reset_position(self):
                self.goto(0,0)
                self.bounce_x()

        #Method to stop the game just in case if players want to
        def game_over(self):
                self.x_move = 0
                self.y_move = 0
                self.home()
                self.color('white')
                self.hideturtle()
                self.write('Bye-bye', align='center', font=('Courier', 50, 'bold'))
                              

                
        