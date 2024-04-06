from turtle  import Turtle

SEGEMTNTS_START_POSITON = [(280, 0), (280, -20), (280, -40)]



MOVE_DISTANCE = 20
Up = 90
Down = 270
# Y_POISITION_TO_MOVE_PADDLE1 = 0
# Y_POISITION_TO_MOVE_PADDLE2 = 0
# X_POISITION_TO_MOVE_PADDLE1 = 440
# X_POISITION_TO_MOVE_PADDLE2 = -440

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)




    def Up(self):
            Y_POISITION_TO_MOVE_PADDLE1 =  self.ycor() + 40
            self.goto(self.xcor(), Y_POISITION_TO_MOVE_PADDLE1)
        # if self.ycor() < 350 :
        # else:
        #     pass
        #     print("pass")

    def Down(self):
            Y_POISITION_TO_MOVE_PADDLE1 = self.ycor() - 40
            self.goto(self.xcor(), Y_POISITION_TO_MOVE_PADDLE1)
            # if self.ycor() < 350:
            # else:
            # pass
            # print("pass")

