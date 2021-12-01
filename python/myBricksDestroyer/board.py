from tkinter import *

class Board:
    def __init__(self, window, width, height, bg):
        self.width = width
        self.height = height
        self.bg = bg

        self.canvas = Canvas(window, width=self.width, height=self.height, bg=self.bg)
        self.canvas.pack()

        font = ("monaco", 12)
        self.scoreboard = self.canvas.create_text(55, 475, font=font, fill="lightgreen")

    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        color = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def draw_plate(self, plate):
        x1 = plate.x_posn
        x2 = plate.x_posn + plate.width
        y1 = plate.y_posn
        y2 = plate.y_posn + plate.height
        color = plate.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="lightyellow")

    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    def delete_item(self, item):
        self.canvas.delete(item)

    def get_coords(self, item):
        return self.canvas.coords(item)

    def draw_score(self, score):
        self.canvas.itemconfigure(self.scoreboard, text=score)
