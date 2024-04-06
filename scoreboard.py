from turtle import  Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.l_score, False, align="center", font=("Courier", 80 , "normal"))
        self.goto(100, 190)
        self.write(self.r_score, False, align="center", font=("Courier", 80, "normal"))
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def gameover(self):
            self.goto(0,0)
            self.write("Game Over ", False, align="center")