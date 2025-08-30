from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from score import score_board
import time
import turtle



my_screen=Screen()
my_screen.bgcolor("black")
my_screen.setup(800,600)
my_screen.tracer(0)



my_ball=Ball()
my_paddle=Paddle()
my_score=score_board()



game_on=True
while game_on:
    my_screen.listen()
    my_screen.onkey(my_paddle.move_right,"Right")
    my_screen.onkey(my_paddle.move_left,"Left")
    time.sleep(0.01)
    
    my_ball.move()

    if my_ball.ycor()>280:
        my_ball.bounce_y()

    if my_ball.ycor()<-250 and my_ball.distance(my_paddle)<50 and my_ball.y_move<0:
        my_ball.bounce_y()
        my_score.update_score()
        my_ball.x_move *= 1.1
        my_ball.y_move *= 1.1


    if my_ball.xcor()>380 or my_ball.xcor()<-380:
        my_ball.bounce_x()

    if my_ball.ycor()<-280:
        my_score.lost()
        name= turtle.textinput("Play Again Input","Do you want to play another game?")

        if name.lower()=="yes" or name.lower()=="y":
            my_ball.reset_ball()
            my_score.reset_score()
            my_paddle.reset_paddle()
            continue
        else:
            
            game_on=False



    my_screen.update()






my_screen.exitonclick()