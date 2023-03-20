from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
food=Food()
snake=Snake()
score=Scoreboard()
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="a",fun=snake.left)
screen.onkey(key="d",fun=snake.right)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.keep_the_score()
        

    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.ycor() <-280 or snake.head.xcor() <-280:
        game_is_on=False
        score.game_over()
    for segment in snake.segments[1:]:        
        if snake.head.distance(segment) <10:
            game_is_on=False
            score.game_over()

    


    
screen.exitonclick()