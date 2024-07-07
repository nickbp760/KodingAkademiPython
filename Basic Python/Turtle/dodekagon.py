import turtle

# Inisialisasi turtle
t = turtle.Turtle()

# Menggambar dodekagon dengan loop
for _ in range(12):
    t.forward(50)
    t.right(30)

# Menutup jendela saat di-klik
turtle.done()
