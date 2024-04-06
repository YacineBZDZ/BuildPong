import turtle as t

import paddle
import paddle as p
PADDLE_START_POSITON = [(440, 0), (-440, 0)]
position_paddel1 = PADDLE_START_POSITON[0]
position_paddel2 = PADDLE_START_POSITON[1]
SCORE = False
Game_On = True
class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        x = self.xcor() + self.x_move
        y = + self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def resetPoistion(self):
        self.goto(0,0)
        self.bounce_x()
