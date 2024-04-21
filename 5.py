"""
    9.25
    author Kalugin Alexander
    email sashakalugin74@gmail.com
    version 3.11 01/03/24
    group 10701223
    What a program that display Traffic light and change color
"""
from tkinter import *

window = Tk()
window.title("Traffic light simulator")
window.geometry("400x700")

def Delete_color():
    canvas.itemconfigure(circle1, fill="gray")
    canvas.itemconfigure(circle2, fill="gray")
    canvas.itemconfigure(circle3, fill="gray")
def Red():
    Delete_color()
    canvas.itemconfigure(circle1, fill="red")
def Yellow():
    Delete_color()
    canvas.itemconfigure(circle2, fill="yellow")
def Green():
    Delete_color()
    canvas.itemconfigure(circle3, fill="green")
canvas = Canvas(window, width=400, height=650)
canvas.pack()
canvas.create_rectangle(100, 50, 300, 650)

circle1 = canvas.create_oval(110, 60, 290, 250, fill="gray", tags="red")
circle2 = canvas.create_oval(110, 260, 290, 450, fill="gray", tags="yellow")
circle3 = canvas.create_oval(110, 460, 290, 640, fill="gray", tags="green")

color = IntVar()
button_red = Radiobutton(window, text="Red", value=1, variable=color, command=Red)
button_red.pack(side=LEFT)

button_yellow = Radiobutton(window, text="Yellow", value=2, variable=color, command=Yellow)
button_yellow.pack(side=LEFT)

button_green = Radiobutton(window, text="Green", value=3, variable=color, command=Green)
button_green.pack(side=LEFT)

window.mainloop()