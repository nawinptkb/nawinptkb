import time
from turtle import Turtle


class Timer(Turtle):
        def __init__(self):
                super().__init__()
                self.start = time.time()
                self.color('DarkSlateGray1')
                self.hideturtle()
                self.penup()
                
        #Initialize the timer
        def writeTime(self):
                self.clear() #Clear the timer everytime the new one is generated (will work in Game.py; in a while loop)
                self.goto(-5,180)                
                self.write(round(float(time.time() - self.start),2),align='center' ,font=("Courier", 30,'normal')) #Generate the timer on the screen 

        #When the game is over, the timer should disappear, doing so by setting the color to black
        def game_over(self):
                self.color('black')

        #Write the text at the start, telling player how to start the game
        def write_text(self):
                self.hideturtle()
                self.goto(0,0)
                self.write('To start, press "c"', align='center', font=('Courier', 30, 'bold'))
                self.goto(0,-50)
                self.write('R_paddle use "e" to go up and "s" to go down', align='center', font=('Courier', 20, 'bold'))
                self.goto(0,-100)
                self.write('L_paddle use "i" to go up and "l" to go down ', align='center', font=('Courier', 20, 'bold'))
                self.goto(0,-150)
                self.color('red')
                self.write('press "space" to stop the game ', align='center', font=('Courier', 20, 'bold'))

                self.color('DarkSlateGray1') #Change the color black to light blue for the timer

        
