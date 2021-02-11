from turtle import Turtle


class ScoreBoard(Turtle):

    ALIGNMENT = 'center'
    FONT = ('Arial', 12, 'normal')

    def __init__(self):
        super().__init__()
        self.result = 0
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f'Score: {self.result}',
            align=ScoreBoard.ALIGNMENT,
            font=ScoreBoard.FONT
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            'GAME OVER',
            align=ScoreBoard.ALIGNMENT,
            font=ScoreBoard.FONT
        )

    def result_add(self):
        self.result += 1
        self.clear()
        self.update_scoreboard()