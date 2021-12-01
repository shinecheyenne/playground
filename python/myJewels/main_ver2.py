#Let's go find some jewels#

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#board
def board():
    global rect_list
    x1 = y1 = 0
    for x in range(10):
        for y in range(10):
            myRect = canvas.create_rectangle((x*50, y*50, (x+1)*50, (y+1)*50), fill="lightblue", tag="rect"+str(10*x+y), outline="lightyellow")
            rect_list.append(canvas.coords("rect"+str(10*x+y)))
            x1+=50
        x1=0
        y1+=50

#Go,go!
def goGo(event):
    global myImage, rect_list, jewel_list, count
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
            #canvas.delete("jewel"+str(coords_jewel.index(i)))
            del jewel_list[coords_jewel.index(i)]
            del coords_jewel[coords_jewel.index(i)]

            print(jewel_list)
            print(coords_jewel)

    for j in rect_list:
        if coords_i == [j[0]+25, j[1]+25]:
            canvas.delete("rect" + str(rect_list.index(j)))

    if len(jewel_list)==0:
        messagebox.showinfo("Congrats!", "All jewels are yours! GOOD bye!")


#field
rect_list = []
jewel_list = ["crown.png", "gem.png", "jewel.png", "jewelry.png", "jewels.png", "ring.png"]
coords_jewel=[]

#main
window = Tk()
window.title("Let's eat some jewels")

canvas = Canvas(window, width = 500, height = 500, bg="lightyellow")
canvas.pack()
board()

# make random tuples
while(len(coords_jewel)!=len(jewel_list)):
    el = (random.randrange(1, 20, 2)*25, random.randrange(1, 20, 2)*25)
    if el not in coords_jewel and el!=(25,475):
        coords_jewel.append(el)
print(coords_jewel)

# display jewels
for k in range(len(jewel_list)):
    jewel_list[k] = ImageTk.PhotoImage(Image.open(jewel_list[k]).resize((25, 25)))
    myJewel = canvas.create_image(coords_jewel[k][0], coords_jewel[k][1], image=jewel_list[k], tag="jewel"+str(k))
    coords_jewel[k]=canvas.coords("jewel"+str(k))

# display angel 
image = Image.open("angel.png")
image = image.resize((25,25))
photo = ImageTk.PhotoImage(image)
myImage = canvas.create_image(25, 475, image=photo, tag="myi")

canvas.bind_all("<KeyPress>", goGo)
window.mainloop()
