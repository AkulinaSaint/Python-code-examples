import turtle
import random
import math
import myrobot

turtle.speed(0)
PHI = 360 / 7
R = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def baraban(x, y):
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(x, y + 160)
    draw_circle(5, 'red')

    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'white')


def baraban_animation(x, y, start):
    for i in range(start, random.randrange(7, 40)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 60)
    draw_circle(22, 'brown')

    return i % 7


baraban(100, 100)

answer = ''
start = 0
while answer != 'n':
    answer = turtle.textinput("Сделать выстрел?", "y/n")

    if answer == 'y':
        start = baraban_animation(100, 100, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))



turtle.exitonclick()