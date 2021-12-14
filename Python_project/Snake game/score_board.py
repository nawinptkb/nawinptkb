from turtle import Turtle

SCORE_ALIGNMENT = "Center"
FONT = ('Arial',21,'normal')
FONT_GAMEOVER = ('Arial',40,'normal')

class Score_Board(Turtle):
        def __init__(self):
                super().__init__()
                self.score = 0

                #with keyword allows the file not to be closed after being done with the editing; python will save the file to the persistent storage itself.
                with open('score_data.txt', mode='r') as score_data:
                        self.high_score = int(score_data.read()) #read the highscore from the score_data.txt and then assign it to the current highscore everytime the game runs
                
                self.color('white')
                self.hideturtle()
                self.penup()
                self.goto(0,270) #Set the position of the scoreboard at the top of the window
                
                self.update_scoreboard()
        
        def update_scoreboard(self):
                self.clear() #Remove the old score board every time the method update_scoreboard is being recalled
                self.color('white')
                self.write(f'Score : {self.score} High Score: {self.high_score}',move=False, align=SCORE_ALIGNMENT, font=FONT)


        #Create the high score saving mechanism
        def reset_scoreboard(self):
                if self.score > self.high_score:
                        self.high_score = self.score #When the current score is higher than the current high score. The high score will be replaced with the current score
                        with open('score_data.txt',mode='w') as score_data:
                                score_data.write(str(self.high_score)) #Overwrite the old highscore in score_data.txt

                self.score = 0 #Set the current the score back to "0" everytime the reset_scoreboard() method is being called.
                self.update_scoreboard() #Update the score board so that the old score gets removed and replaced by a new one.


        def increase_score(self):
                self.score += 1
                self.update_scoreboard() #Create a newly updated scoreboard at the same position as the previous one