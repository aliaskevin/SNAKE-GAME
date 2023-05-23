from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 280)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 10, 'bold'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 10, 'bold'))
