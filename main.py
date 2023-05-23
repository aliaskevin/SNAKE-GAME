from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
game_is_on = True
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.next_move()
    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()
    # Detect wall collision
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()
    # Detect tail collision
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False
screen.exitonclick()
