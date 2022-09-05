from turtle import *

speed(30)


def draw_square():
    begin_fill()
    for i in range(4):
        color("aqua")
        width(3)

        forward(250)
        left(90)
    end_fill()


penup()
goto(-150, -150)
pendown()

draw_square()


def draw_triangle():
    begin_fill()
    for i in range(3):
        width(3)
        color("red")
        forward(250)
        left(120)

    end_fill()


penup()
goto(-150, 100)
pendown()


draw_triangle()


def draw_door():
    begin_fill()
    for i in range(4):
        width(2)
        color("black")
        forward(120)
        left(90)
    end_fill()


penup()
goto(-80, -150)
width()
pendown()

draw_door()


def draw_window():
    begin_fill()
    for i in range(4):
        width(1)
        color("blue")
        forward(60)
        left(90)
    end_fill()


penup()
goto(30, -10)
pendown()

draw_window()


def draw_window2():
    begin_fill()
    for i in range(4):
        color("blue")
        forward(60)
        left(90)
    end_fill()


penup()
goto(-140, -10)
pendown()

draw_window2()


def draw_fireplace():
    begin_fill()
    for i in range(1):

        color("brown")

        left(90)
        forward(45)
        right(90)
        forward(42)
        right(90)
        forward(126)
    end_fill()


penup()
goto(60, 170)
pendown()

draw_fireplace()


exitonclick()