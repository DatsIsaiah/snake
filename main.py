from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right, "d")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collecting food
    if snake.head.distance(food) < 15 :
        snake.extend()
        food.refresh()
        scoreboard.add_point()

    #Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        scoreboard.gameover()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameover()


screen.exitonclick()
