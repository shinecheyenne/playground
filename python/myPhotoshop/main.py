from tkinter import *
from tkinter.filedialog import *  # 파일 입출력
from tkinter.simpledialog import *  # 숫자나 문자 입출력창
from PIL import Image, ImageTk, ImageEnhance
import random
import re

###method
def display(img):
    global window, r_frame, canvas, width, height, photo, photo2,original, x, y, text, filename
    photo2 = ImageTk.PhotoImage(img)
    canvas.create_image((x, y), image=photo2, state="normal", tag="myPhoto")
    canvas.delete("text")
    canvas.create_text(90, 60, text=filename, fill="white", font= ("Courier", 20), tag="text")

def file_open():
    global window, r_frame, canvas, width, height, photo, photo2,original, x, y, filename
    file_path = askopenfilename(filetypes=[("jpb files", "*.jpg"), ("png files", "*.png"), ("All files", "*.*")])
    photo = Image.open(file_path)
    filename = photo.filename.split("/")[-1]
    filename = re.split(r'\.', filename)[0]
    width = 500
    height = int(photo.size[1]/photo.size[0]*width)
    photo = photo.resize((width, height), Image.ANTIALIAS)
    original = photo
    display(photo)

def file_save():
    global window, r_frame, canvas, width, height, photo, photo2,original, x, y
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg",
                           filetypes=(("JPG files", ("*.jpg", '*.jpeg')), ("All files", "*.*")))
    photo.save(saveFp.name)

def func_revert():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    x, y = 400, 400
    photo = original
    display(original)

def func_move():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    def click(event):
        global x, y
        x, y = event.x, event.y

        canvas.delete("myPhoto")
        canvas.create_image((x, y), image=photo2, state="normal", tag="myPhoto")  # width/2, height/2: paper의 canvas상 위치

    canvas.bind("<B1-Motion>", click)

def func_exit():
    window.quit()
    window.destroy()

def func_resize():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    scale = askinteger("scale", "percentage: ", minvalue=25, maxvalue=200)
    width = int(width*scale/100)
    height = int(height*scale/100)
    photo=photo.resize((width, height), Image.ANTIALIAS)
    display(photo)

def func_rotatecounter():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = photo.transpose(Image.ROTATE_90)
    display(photo)

def func_rotate():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = photo.transpose(Image.ROTATE_270)
    display(photo)

def func_flip():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = photo.transpose(Image.FLIP_LEFT_RIGHT)
    display(photo)

def func_flop():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = photo.transpose(Image.FLIP_TOP_BOTTOM)
    display(photo)

def func_crop():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y, x1, x2, y1, y2
    def mouseOn(event):
        global x1, y1
        x1, y1 = event.x, event.y

    def mouseDrag(event):
        global x1, y1, x2, y2
        x2, y2 = event.x, event.y
        canvas.create_line((x1,y1, x2, y1), fill="#6a6a6a", width=1, tag="line")
        canvas.create_line((x1,y1, x1, y2), fill="#6a6a6a", width=1, tag="line")

    def mouseRelease(event):
        global x1, y1, x2, y2, photo, height
        x2, y2 = event.x, event.y
        canvas.create_rectangle((x1, y1, x2, y2), outline="#6a6a6a", width=1, tag="rect")
        box = (x1-150,y1-int((800-height)/2),x2-150,y2-int((800-height)/2))
        photo = photo.crop(box)
        canvas.delete("line")
        canvas.delete("rect")
        display(photo)

    canvas.bind("<Button>", mouseOn)
    canvas.bind("<B1-Motion>", mouseDrag)
    canvas.bind("<ButtonRelease-1>", mouseRelease)

def func_rgbplay():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    r, g, b = photo.split()
    randoml = [(r,g,b), (r,b,g), (b,r,g), (b,g,r), (g,r,b), (g,b,r)]
    photo = Image.merge("RGB", randoml[random.randint(0,5)])
    display(photo)

def func_contrastplus():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Contrast(photo).enhance(1.3)
    display(photo)

def func_contrastminus():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Contrast(photo).enhance(0.7)
    display(photo)

def func_brighten():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Brightness(photo).enhance(1.2)
    display(photo)

def func_dark():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Brightness(photo).enhance(0.8)
    display(photo)

def func_sharpen():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Sharpness(photo).enhance(1.4)
    display(photo)

def func_blur():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = ImageEnhance.Sharpness(photo).enhance(0.6)
    display(photo)

def func_mono():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    photo = photo.convert('L')
    display(photo)

def func_pen():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    def paint(event):
        x1, y1 = event.x-1, event.y-1
        x2, y2 = event.x+1, event.y+1
        colorlist=["lightgreen", "lightblue", "pink", "lightyellow"]
        randi = random.randint(0,3)
        canvas.create_oval(x1, y1, x2, y2, fill=colorlist[randi], outline=colorlist[randi], width=5, tag="myPen")
    canvas.bind("<B1-Motion>", paint)

def func_clear():
    canvas.delete("myPen")

def menu_create():
    global window, r_frame, canvas, width, height, photo, photo2, original, x, y
    mainMenu = Menu(window)
    window.config(menu=mainMenu)
    filelist = {"Open": file_open, "Save": file_save, "Close": func_exit}
    editlist = {"Revert":func_revert, "Move": func_move, "Resize":func_resize, "Crop":func_crop,
                "Flip Horizontal": func_flip, "Flip Vertical": func_flop,
                "Rotate Counter Clockwise": func_rotatecounter, "Rotate Clockwise": func_rotate}
    imagelist = {"RGB Play": func_rgbplay, "Contrast >>":func_contrastplus, "Contrast <<":func_contrastminus, "Brighten": func_brighten,
                 "Darken": func_dark, "Sharpen": func_sharpen, "Blur": func_blur, "Black&White": func_mono}
    paintlist = {"Pen": func_pen, "Erase":func_clear}
    def menu_add(parent, labelN, commandN):
        parent.add_command(label=labelN, command=commandN)

    def whatMenu(menu, name, llist):
        menu = Menu(mainMenu, tearoff=0)
        mainMenu.add_cascade(label=name, menu=menu)
        for key in llist:
            menu_add(menu, key, llist[key])

    whatMenu("fileMenu", "File", filelist)
    whatMenu("editMenu", "Edit", editlist)
    whatMenu("imageMenu", "Image", imagelist)
    whatMenu("paintMenu", "Paint", paintlist)

# def btn_create():
#     for i in range(20):
#         button = Button(canvas2, text="↶", height=2, bg="#454545", relief='flat',
#                         command=func_revert)
#         button.pack(side=TOP, anchor=W, ipadx=10)

###field
window, r_frame, canvas, = None, None, None
photo, photo2, original = None, None, None
width, height, x, y = 0, 0, 400, 400
x1 = y1 = x2 = y2 = 0
text, filename =None, None

###main
window = Tk()
window.geometry("800x800")
window.title("My Photoshop")
window.resizable(False, False)

#l_frame = Frame(window, relief='flat', width=40, height=800)
#l_frame.pack(side='left', fill='both')
r_frame = Frame(window, relief='flat', width=800, height=800)
r_frame.pack()
canvas = Canvas(r_frame, width=800, height=800, bd=0, highlightthickness=0, bg='#6a6a6a')
#canvas2 = Canvas(l_frame, width=0, height=800, bd=0, highlightthickness=0, bg='#454545')
backImg = PhotoImage(file ="img/backImg.png")
canvas.create_image((400, 400), image=backImg, state="normal")
canvas.pack()
#canvas2.pack()

menu_create()
# btn_create()

window.mainloop()
