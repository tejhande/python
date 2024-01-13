import turtle

def draw_heart():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")

    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-112,70)
    turtle.left(70)
    turtle.circle(-112,70)
    turtle.forward(224)

    turtle.end_fill()
    turtle.done()

draw_heart()
