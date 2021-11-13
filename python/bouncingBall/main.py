#Bouncing Ball#

from tkinter import *
import random
import time

def ball_move():
    global ball, x, y, coords_list
    coords = canvas.coords(ball)

    if coords[0]<=0 or coords[2]>=500:
        x = -x
    if coords[1]<=0 or coords[3]>=400:
        y = -y
    canvas.move(ball, x, y)

    for i in coords_list:
        if ((coords[0]>=i[0] and coords[0]<=i[2])and(coords[1]>=i[1] and coords[1]<=i[3])):
            canvas.delete("rect"+str(coords_list.index(i)))

window, canvas = None, None
x = y = random.randint(5,10)

window = Tk()
window.title("Bouncing, bouncing ball...")
window.geometry("500x400")
window.resizable(False, False)
canvas = Canvas(window, width=500, height=400, bg="navy")
coords_list=[]

for i in range(10):
    x1 = random.randint(0, 470)
    y1 = random.randint(0, 370)
    canvas.create_rectangle((x1, y1, x1 + 30, y1 + 30), fill="yellow", tag="rect"+str(i), outline="white")
    coords_r = canvas.coords("rect"+str(i))
    coords_list.append(coords_r)
print(list(coords_list))

ball = canvas.create_oval(100,100,110,110, fill="white")
canvas.pack()

while(True):
    ball_move()
    window.update()
    time.sleep(0.02)

window.mainloop()
