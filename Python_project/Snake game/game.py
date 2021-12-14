from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from score_board import Score_Board

#Setup the screen size, background, and title name
screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Just making the snake move smoother

#Create instances of snake, food, and score_board from each class
snake = Snake()
food = Food()
score_board = Score_Board()

screen.listen()#Making the screen to monitor the keyboard
screen.onkey(fun=snake.up , key='w')
screen.onkey(fun=snake.left , key='a')
screen.onkey(fun=snake.down , key='s')
screen.onkey(fun=snake.right , key='d')


SPEED = 0.1 #Speed of the screen update rate (the smaller the smoother)
game_is_on = True
while game_is_on:
        #Update the screen every 0.1 sec to make the movement of the snake smoother
        screen.update()
        time.sleep(SPEED)

        #Make the snake move
        snake.move()

        #Detect collision with food and add another segment(length) everytime it eats the food
        if snake.head.distance(food) < 15: #The distance method will check the distance between the snake head and the food so we set it to 15 pixels just to make it sensitive and easy for the snake to not having to pass through the food diameter
                food.refresh_food() # Rerandom the location of the food everytime the snake head collide with the food
                snake.extend() #Add another segment to the snake everytime it eats the food; by adding a new segment to the position of the last segment
                score_board.increase_score() #Increment the score by 1 everytime the food was eaten
                print('the snake eats the food')

        #Detect collision with wall
        if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
                score_board.reset_scoreboard()
                snake.reset_snake()
                print("The snake collides with the wall")
        
        #Detect collision with its own tail; if the head collides with any segment, the game will stop
        for segment in snake.segments[1:]: #Checking if the element that we are looping through is the (0,0) or snake's head position and then bypass it so when the game start, we don't get a game over. So we, instead, start the loop from the index "1" instead of index "0"
                if snake.head.distance(segment) < 10:
                        score_board.reset_scoreboard() 
                        snake.reset_snake()
                        print("The snake ate its own tail")




        
screen.exitonclick()

