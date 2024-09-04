from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball((0, 0))

# global game_is_on

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(toggle_pause, "space")



game_is_on = True
while game_is_on:
    if not is_paused:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        #detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        #detection with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        #R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        #L paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()

    else:
        screen.update()



screen.exitonclick()

