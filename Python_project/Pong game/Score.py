from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 70, 'normal')

class Score_board(Turtle):
        def __init__(self):
                super().__init__()
                self.color('white')
                self.penup()
                self.hideturtle()
                

                self.l_score = 0 #Score of the left paddle
                self.r_score = 0 #Score of the right paddle
                self.update_scoreboard() 

        
        def update_scoreboard(self):
                #Clear the scoreboard everytime after the score increase to replace the previous scoreboard
                self.clear()

                #Text "Score"
                self.goto(-1,240)
                self.write('Score', align='center', font=('Courier', 30, 'bold'))

                #Scoreboard of the left paddle
                self.goto(-100, 200)
                self.write(self.l_score, align=ALIGNMENT, font=FONT)

                #Scoreboard of the right paddle
                self.goto(100, 200)
                self.write(self.r_score, align=ALIGNMENT, font=FONT)


        def givePointToLeftPaddle(self):
                self.l_score += 1
                self.update_scoreboard() #Update a score board after the point has been given

        def givePointToRightPaddle(self):
                self.r_score += 1
                self.update_scoreboard() #Update a score board after the point has been given

 


                