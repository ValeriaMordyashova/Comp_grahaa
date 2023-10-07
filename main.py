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


def exit_program(event):
    if event.keysym == "Escape":
        window.quit()

# Привязываем клавиши к функциям
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Escape>", exit_program)


window.mainloop()

