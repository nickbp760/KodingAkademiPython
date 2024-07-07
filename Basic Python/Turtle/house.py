import turtle

# Inisialisasi turtle
t = turtle.Turtle()
# memakai 3, 4, 5 untuk segitiga
# Menggambar atap trapesium
t.penup()
t.goto(-100, 100)
t.pendown()
t.begin_fill()
if True:
    t.fillcolor("red")
    t.forward(200)
    t.right(53)
    t.forward(150)
    t.right(127)
    t.forward(380)
    t.right(127)
    t.forward(150)
    t.right(53)
t.end_fill()

# Menggambar bagunan persegi panjang
t.penup()
t.goto(-100, -20)
t.pendown()
t.begin_fill()
if True:
    t.fillcolor("blue")
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

# Menggambar pintu persegi
t.penup()
t.goto(-25, -170)
t.pendown()
t.begin_fill()
if True:
    t.fillcolor("yellow")
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()
turtle.done()
