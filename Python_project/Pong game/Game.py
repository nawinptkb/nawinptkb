from turtle import Turtle, Screen
from Paddle import *
from Ball import *
from Score import *
import time
from Timer import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong-Game")
screen.tracer(0) #Just making everything move smoothly by turning off the animation refreshment; but we also need to update the screen manually


#Our 2 controllable paddles
l_paddle = Paddle(-370,0)
r_paddle = Paddle(370,0)
#A ball
ball = Ball()
#Scoreboard
score_board = Score_board()
#Timer
timer = Timer()
timer.write_text() #Write the starting text

#Function start to start the game
def start():
        game() #Activate the game

#Function gameover to stop the game
def game_over():
        ball.game_over() #Stop the motion of the ball and bring it to the middle of the screen
        timer.game_over() #Stop the timer 


#Activating the keyboard tracker
screen.listen()
screen.onkey(fun=l_paddle.go_up, key="e")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="i")
screen.onkey(fun=r_paddle.go_down, key="l")
screen.onkey(fun=game_over, key='space') #On spacebar, players are able to stop the game whenever they want
screen.onkey(fun=start, key='c') #On key "c", the game will start

BALL_SPEED = 0.05
"""Game Activation Section"""
def game():
        game_is_on = True

        while game_is_on:
                time.sleep(BALL_SPEED) #Make the time sleep for a bit after each iteration (This also control the speed of the ball)
                screen.update() #Update the animation manually since we turn off the animation by setting screen.tracer(0); will update the scoreboard, timer, and the rest that are texts
                timer.writeTime() #Initialize the timer
                ball.move() #Activate the movement of the ball


                #Detect collision of the ball with top and bottom wall 
                if ball.ycor() >= 280 or ball.ycor() <= -280:
                        #Bouncing the ball
                        ball.bounce_y()
                        

                """The best distance between the ball and the paddles is 50px since it covers all the possibility 
                and direction that the ball will collide with the paddles"""
                #Detect collision of the ball with the Right paddle
                if ball.distance(r_paddle) < 50 and ball.xcor() > 310:
                        ball.bounce_x()
                        

                #Detect collision of the ball with the Left paddle
                elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
                        ball.bounce_x()
                        

                #Detect if the Right paddle misses the ball
                if ball.xcor() > 380:
                        ball.reset_position()
                        score_board.givePointToLeftPaddle()
                
                #Detect if the Left paddle misses the ball
                elif ball.xcor() < -380:
                        ball.reset_position()
                        score_board.givePointToRightPaddle()

                #If any player score more than 19, the game will be over 
                if score_board.l_score >= 10 or score_board.r_score >= 10:
                        ball.game_over()
                        timer.game_over()
                


                
screen.exitonclick()