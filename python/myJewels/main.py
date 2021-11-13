#Let's go find some jewels#

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#board
def board():
    # ##maze
    # maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #         [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    #         [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    #         [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    #         [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    #         [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    #         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    #         [1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]
    #
    # for y in range(10):
    #     for x in range(10):
    #         if maze[y][x]==1:
    #             canvas.create_rectangle((x*50, y*50, (x+1)*50, (y+1)*50), fill="salmon", tag="rect" + str(10*y+x),
    #                                     outline="lightyellow")

    global rect_list
    x1 = y1 = 0
    for x in range(10):
        for y in range(10):
            myRect = canvas.create_rectangle((x*50, y*50, (x+1)*50, (y+1)*50), fill="salmon", tag="rect"+str(10*x+y), outline="lightyellow")
            rect_list.append(canvas.coords("rect"+str(10*x+y)))
            x1+=50
        x1=0
        y1+=50

#Go,go!
def goGo(event):
    global myImage, rect_list
    coords_i = canvas.coords("myi")
    if event.keysym == "Up":
        canvas.move(myImage, 0, -25)
    if event.keysym == "Down":
        canvas.move(myImage, 0, 25)
    if event.keysym == "Left":
        canvas.move(myImage, -25, 0)
    if event.keysym == "Right":
        canvas.move(myImage, 25, 0)

    for i in coords_jewel:
        if coords_i == i:
            canvas.delete("jewel"+str(coords_jewel.index(i)))

    for j in rect_list:
        if coords_i == [j[0]+25, j[1]+25]:
            canvas.delete("rect" + str(rect_list.index(j)))

#field
rect_list = []
jewel_list = ["crown.png", "gem.png", "jewel.png", "jewelry.png", "jewels.png", "ring.png"]
coords_jewel=[]

#main
window = Tk()
window.title("Let's move")

canvas = Canvas(window, width = 500, height = 500, bg="lightyellow")
canvas.pack()
board()

for k in range(len(jewel_list)):
    jewel_list[k] = ImageTk.PhotoImage(Image.open(jewel_list[k]).resize((25, 25)))
    myJewel = canvas.create_image(random.randrange(1, 20, 2)*25, random.randrange(1, 20, 2)*25, image=jewel_list[k], tag="jewel"+str(k))
    coords_jewel.append(canvas.coords("jewel"+str(k)))

image = Image.open("angel.png")
image = image.resize((25,25))
photo = ImageTk.PhotoImage(image)
myImage = canvas.create_image(25, 475, image=photo, tag="myi")

canvas.bind_all("<KeyPress>", goGo)
window.mainloop()