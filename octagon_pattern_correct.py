import turtle as tt


def unit_pat(turtlename, length, loopcounter):
    # turtlename = tt.Turtle()
    if loopcounter > 0:
        turtlename.right(180)
    turtlename.forward(length)
    turtlename.left(45)
    turtlename.forward(length)
    turtlename.right(90)
    turtlename.forward(length)
    turtlename.left(135)
    turtlename.forward(length)
    turtlename.left(45)
    turtlename.forward(length)
    turtlename.left(135)
    turtlename.forward(length)
    turtlename.right(90)
    turtlename.forward(length)
    turtlename.left(45)
    turtlename.forward(length)


def draw_art():
    window = tt.Screen()
    lt = tt.Turtle()
    lt.speed('normal')
    for i in range(8):
        unit_pat(lt, 30, i)
    window.exitonclick()
draw_art()
