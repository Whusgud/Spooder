import turtle as trtl

painter = trtl.Turtle()

#settings
w = 6
z = 300 / w
n = 0
y = 70

x = 4
t = 0
o = 180 / x

q = 4
e = 0
r = 180/q
painter.speed(0)

painter.penup()
painter.goto(0, -700)
painter.color("bisque4")
painter.begin_fill()
painter.circle(1000)
painter.end_fill()

painter.penup()
painter.goto(0, -400)
painter.left(30)
painter.color("brown")
painter.begin_fill()
painter.circle(1000)
painter.end_fill()

painter.penup()
painter.goto(0, -100)
painter.right(30)
painter.color('black')
painter.begin_fill()
painter.circle(150)
painter.end_fill()

while n < w:
  painter.penup()
  painter.goto(0,30)
  painter.setheading(z*n)
  painter.forward(y)
  painter.pendown()
  painter.color('black', 'red')
  painter.begin_fill()
  painter.circle(20)
  painter.end_fill()
  n = n + 1

while (t < x):
  painter.pensize(20)
  painter.penup()
  painter.goto(70, 80)
  painter.setheading(o*t)
  painter.forward(y)
  painter.pendown()
  painter.color('black')
  painter.right(30)
  painter.forward(60)
  painter.right(30)
  painter.forward(60)
  t = t + 1

while (e < q):
  painter.pensize(20)
  painter.penup()
  painter.goto(-35, -25)
  painter.setheading(r*e)
  painter.back(y)
  painter.pendown()
  painter.color('black')
  painter.right(20)
  painter.back(60)
  painter.left(30)
  painter.back(60)
  e = e + 1

painter.penup()
painter.goto(-275, 350)
painter.color("red")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()