from tkinter import *
import board, ball, plate
from PIL import Image, ImageTk


window = Tk()
window.title("Bricks Destroyer")
window.resizable(False, False)
my_board = board.Board(window, 500, 500, "lightyellow")

_x, _y = 5, 5
first_serve = True


my_ball = ball.Ball(board=my_board, width=10, height=10, color="lightgreen", x_posn=250, y_posn=470, x=10, y=5)#####
my_plate = plate.Plate(board=my_board, width=100, height=5, color="lightblue", x_posn=205, y_posn=480)

#make my character
image = Image.open("angel.png")
image = image.resize((15, 15))
photo = ImageTk.PhotoImage(image)
my_board.canvas.create_image(25 ,475, image=photo)


# make bricks
b_list = []

def make_bricks(k_v, m_v):
    for k in range(k_v):
        for m in range(m_v):
            b_list.append(plate.Plate(board=my_board, width=20, height=10, color="salmon", x_posn=m * 20, y_posn=k * 20))
    return b_list

make_bricks(15,25)


def game_flow():
    global first_serve
    
    if first_serve == True:
        my_ball.stop_ball()
        my_board.draw_score("go!")
        first_serve = False
    my_plate.detect_collision(my_ball)
  
    for b in b_list:
        if b.detect_collision(my_ball)!=None:
            my_board.delete_item(b.plate)
            b_list.remove(b)
            
    if my_ball.y_posn >= my_board.height - my_ball.height:
        my_ball.stop_ball()
        my_ball.default_position()
        my_plate.to_default_position()
        
    if len(b_list)==0:
        make_bricks(15,25)
        my_ball.stop_ball()
        my_ball.default_position()
        my_plate.to_default_position()
        my_board.draw_score("end")
        first_serve = True
        
    if 15 * 25 - len(b_list)!=0:
        my_board.draw_score("+" + str(15 * 25 - len(b_list)))
        
    my_ball.move_ball()    
    window.after(10, game_flow)

def restart_game(event):
    my_ball.start_ball(x=_x, y=_y)
    my_plate.to_default_position()
    

window.bind_all("<KeyPress>", my_plate.move_plate)
window.bind("<space>", restart_game)

game_flow()
window.mainloop()
