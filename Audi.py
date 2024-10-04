#MehtabCodes Presents
#Audi Logo Using Python Turtle

import turtle as tk

tk.pensize(5)
tk.Screen().bgcolor("black")
tk.pencolor("#fff")
tk.speed(10)

for i in range(4):
  tk.penup()
  tk.goto(i*70, 0)
  tk.pendown()
  tk.circle(50)

tk.color("white")
tk.penup()
tk.goto(77, -40)
tk.pendown()
tk.hideturtle()
tk.done()