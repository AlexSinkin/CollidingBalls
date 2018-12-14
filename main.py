import tkinter as tk
from random import *
from ball import *


checked_ball_pairs = []


def create_window():
    global window, canv
    window = tk.Tk()
    window.geometry("{}x{}".format(window_width, window_height))
    canv = tk.Canvas(window, width=window_width, height=window_height)
    canv.pack()
    canv.create_rectangle(2, 2, window_width, window_height)


def clear_checked_pairs():
    global checked_ball_pairs
    checked_ball_pairs = []


def ball_pair_checked(ball1, ball2):
    for ball_pair in checked_ball_pairs:
        if ball_pair[0] == ball1 and ball_pair[1] == ball2 or \
           ball_pair[0] == ball2 and ball_pair[1] == ball1:
            return True
        else:
            checked_ball_pairs.append((ball1, ball2))
            return False


def timer_cycle():
    global window, balls_array
    for ball in balls_array:
        ball.move()

        for wall in [(2, None), (window_width, None), (None, 2), (None, window_height)]:
            if ball.collide_with_wall(wall):
                ball.bounce_off_wall(wall)
                ball.check_glue_to_wall(wall)

        clear_checked_pairs()

        for ball2 in balls_array:
            if ball2 != ball and not ball_pair_checked(ball, ball2):
                if ball.collide_with_ball(ball2):
                    ball.bounce_off_ball(ball2)

    window.after(10, timer_cycle)
    return


window_width = 1200
window_height = 500

window = None
canv = None

create_window()

# рисуем шары.

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'brown', 'pink']
balls_array = []

n_balls = 10
for i in range(n_balls):
    balls_array.append(Ball(canv,
                            randint(50, 850),
                            randint(50, 550),
                            30,
                            randint(-5, 5),
                            randint(-5, 5),
                            choice(colors)))

window.after(10, timer_cycle)
window.mainloop()
