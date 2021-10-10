##Very Basic Calculator

'''
#plan#
1. remove margin between buttons
2. need rounding off and fix the right-position of the entry space
3. add del-key
4. hide cursor
5. change button color on mac os
6. simplify code (buttons)
7. bind clearClick and esc-key
'''

from tkinter import *

#function
def calc(event) :
    result = str(eval(t_exp.get()))
    entry_text.set(result)       
    t_exp.icursor('end')
    
def onClick(self):
    add_text = self["text"]
    t_exp.insert("end",add_text)
    t_exp.icursor('end')
    

def clearClick():
    t_exp.delete(0,"end")
    

def equalClick():
    result = str(eval(t_exp.get()))
    entry_text.set(result)   
    t_exp.bind("<Return>", calc)
    t_exp.icursor('end')

def percent(event):
    result = str(eval(t_exp.get()))
    entry_text.set(float(result)/100)
    t_exp.icursor('end')

def sign(event):
    result = str(eval(t_exp.get()))
    entry_text.set(float(result)*(-1))
    t_exp.icursor('end')
    
#tkinter
root = Tk()
root.title("Very Basic Calculator")
root.geometry("268x350")
root.resizable(False, False)

#disposition
t_frame = Frame(root, relief='flat', width=268, height=70)
t_frame.pack(side='top', fill='both')
b_frame = Frame(root, relief='flat', width=268, height=280)
b_frame.pack(side='bottom', fill='both')

#input and output
entry_text = StringVar()
t_exp = Entry(t_frame, relief='flat', font=('arial', 30), bd=27, textvariable=entry_text, justify='right', bg='light gray', highlightthickness=0)
t_exp.focus()
t_exp.bind("<Return>", calc)
t_exp.pack()

#buttons
parameters = {'height':3, 'width':7}
buttonclear = Button(b_frame, text="C", **parameters, command=clearClick); buttonclear.grid(row=0,column=0)
buttonsign = Button(b_frame, text="+/-", **parameters); buttonsign.grid(row=0,column=1)
buttonsign.bind("<Button-1>", sign)
buttonper = Button(b_frame, text="%", **parameters); buttonper.grid(row=0,column=2)
buttonper.bind("<Button-1>", percent)
buttondiv = Button(b_frame, text="/", **parameters, command=lambda: onClick(buttondiv)); buttondiv.grid(row=0,column=3)
button1 = Button(b_frame, text="1", **parameters, command=lambda: onClick(button1)); button1.grid(row=1,column=0)
button2 = Button(b_frame, text="2", **parameters, command=lambda: onClick(button2)); button2.grid(row=1,column=1)
button3 = Button(b_frame, text="3", **parameters, command=lambda: onClick(button3)); button3.grid(row=1,column=2)
buttonmul = Button(b_frame, text="*", **parameters, command=lambda: onClick(buttonmul)); buttonmul.grid(row=1,column=3)
button4 = Button(b_frame, text="4", **parameters, command=lambda: onClick(button4)); button4.grid(row=2,column=0)
button5 = Button(b_frame, text="5", **parameters, command=lambda: onClick(button5)); button5.grid(row=2,column=1)
button6 = Button(b_frame, text="6", **parameters, command=lambda: onClick(button6)); button6.grid(row=2,column=2)
buttonmin = Button(b_frame, text="-", **parameters, command=lambda: onClick(buttonmin)); buttonmin.grid(row=2,column=3)
button7 = Button(b_frame, text="7", **parameters, command=lambda: onClick(button7)); button7.grid(row=3,column=0)
button8 = Button(b_frame, text="8", **parameters, command=lambda: onClick(button8)); button8.grid(row=3,column=1)
button9 = Button(b_frame, text="9", **parameters, command=lambda: onClick(button9)); button9.grid(row=3,column=2)
buttonplus = Button(b_frame, text="+", **parameters, command=lambda: onClick(buttonplus)); buttonplus.grid(row=3,column=3)
button0 = Button(b_frame, text="0", **parameters, command=lambda: onClick(button0)); button0.grid(row=4,column=0,columnspan=2,ipadx=3) 
button0.config(width=14, padx=0)
buttonp = Button(b_frame, text=".", **parameters, command=lambda: onClick(buttonp)); buttonp.grid(row=4,column=2)
buttoneql = Button(b_frame, text="=", **parameters, command=equalClick); buttoneql.grid(row=4,column=3)


root.mainloop()
