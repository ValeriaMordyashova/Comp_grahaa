from tkinter import *
from tkinter import Tk

window = Tk()
window.title("Лабораторная работа №1")
window.geometry('500x500')
a=10
b=10
c=20
canvas_width = 150
canvas_height =150
python_green = "#476042" # ID цвета обводки.

w = Canvas(window,
           width=500,
           height=500)
w.pack()

points = [a, b, canvas_width, canvas_height / 2, c, canvas_height]
triangle = w.create_polygon(points, outline=python_green, fill='green', width=3)

# Функции для изменения позиции треугольника
def move_left(event):
    w.move(triangle, -3, 0)

def move_right(event):
    w.move(triangle, 3, 0)

def move_up(event):
    w.move(triangle, 0, -3)

def move_down(event):
    w.move(triangle, 0, 3)

# Привязываем клавиши к функциям
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

window.mainloop()

""""

window.pack(fill=BOTH, expand=1)

canvas = Canvas(window)
canvas.create_line(15, 25, 200, 25)
canvas.create_line(300, 35, 300, 200, dash=(4, 2))
canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

canvas.pack(fill=BOTH, expand=1)



"from tkinter import *

root = Tk()

canvas = Canvas(root)

hx = 10
hy = 10
x1 = 20
y1 = 20
x2 = 300
y2 = 200

def draw(event):
    print('a')
    global hx, hy, x1, y1, x2, y2
    x1 += hx
    y1 += hy
    x2 -= hx
    y2 -= hy
    canvas.create_rectangle(x1, y1, x2, y2, outline="black")

def close(event):
    print('b')
    root.destroy()

canvas.bind('<Enter>', draw)
canvas.bind('<Escape>', close)

canvas.pack(fill=BOTH, expand=1)
root.mainloop()"""
