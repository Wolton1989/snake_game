from turtle import Screen
from Snake import Snake
from food import Food
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Wally Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detects collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detects collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detects  collision with tail
    for segmant in snake.segments[1:]:
        if snake.head.distance(segmant) < 10:
            game_is_on = False
            score.game_over()









screen.exitonclick()

