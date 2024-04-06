import time
import turtle as t
import ball as b
import paddle as p
import scoreboard as s

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


screen_diviser = [(0, 360), (0, 300), (0, 240), (0, 180), (0, 120), (0, 60), (0, 0), (0, -60), (0, -120), (0, -180), (0, -240),
                 (0, -300), (0, -360)]

PADDLE_START_POSITON = [(350, 0), (-350, 0)]

position_paddel1 = PADDLE_START_POSITON[0]
position_paddel2 = PADDLE_START_POSITON[1]
def create_screen(position):
    new_diviser = t.Turtle("square")
    new_diviser.shapesize(1, 0.3)
    new_diviser.resizemode("user")
    new_diviser.color("white")
    new_diviser.penup()
    new_diviser.speed("fastest")
    new_diviser.goto(position)




for position in screen_diviser:
    create_screen(position)

paddle2 = p.Paddle(position_paddel2)
paddle1 = p.Paddle(position_paddel1)
ball = b.Ball()
score  = s.ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and paddle1.xcor() > 320 or ball.distance(paddle2) < 50 and paddle2.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.resetPoistion()
        score.l_point()
    elif ball.xcor() < -380 :
       ball.resetPoistion()
       score.r_point()

    screen.listen()
    screen.onkey(paddle1.Up, "Up")
    screen.onkey(paddle2.Up, "z")
    screen.onkey(paddle1.Down, "Down")
    screen.onkey(paddle2.Down, "s")



screen.exitonclick()