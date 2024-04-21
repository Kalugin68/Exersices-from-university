"""
    9.17
    author Kalugin Alexander
    email sashakalugin74@gmail.com
    version 3.11 01/03/24
    group 10701223
    Write a program that display car
"""
from tkinter import *


def draw_car(x, y):
    canvas.create_rectangle(x, y - 20, x + 50, y - 10, fill="grey")
    canvas.create_oval(x + 10, y, x + 20, y - 10, fill="black")
    canvas.create_oval(x + 30, y, x + 40, y - 10, fill="black")
    points = ((x + 20, y - 30), (x + 30, y - 30), (x + 40, y - 20), (x + 10, y - 20))
    canvas.create_polygon(points, fill="grey", outline="black")


def new_window():
    global car_x, car_speed

    car_x += car_speed

    if car_x > width:
        car_x = -50

    canvas.delete("all")
    draw_car(car_x, car_y)

    window.after(10, new_window)


def speed_change(event):
    global car_speed

    if event.keysym == "Up" and car_speed < 10:
        car_speed += 1
    elif event.keysym == "Down" and car_speed > 1:
        car_speed -= 1


width = 400
height = 300

car_x = 0
car_y = height
car_speed = 5

window = Tk()
window.title("Racing Car")

canvas = Canvas(window, width=width, height=height)
canvas.pack()

new_window()

window.bind("<Up>", speed_change)
window.bind("<Down>", speed_change)

window.mainloop()