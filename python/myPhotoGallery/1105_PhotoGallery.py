from tkinter import *
from tkinter import messagebox


##변수선언
fnameList=[]
for i in range(6):
    fnameList.append("Photo "+str(i+1)+".png");
    
num = 0

## 함수 선언
def clickNext():
    global num # 전역변수를 함수 안에서 사용하겠다
    num+=1
    if num>5:
        num=0
    photo = PhotoImage(file = "gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo#++
    text.configure(text=fnameList[num])

def clickPrev():
    global num
    num-=1
    if num<0:
        num=5
    photo = PhotoImage(file = "gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    text.configure(text=fnameList[num])

def pageRight(event):
    clickNext()
    
def pageLeft(event):
    clickPrev()

#환영인사
def clickClick(event):
    messagebox.showinfo("Welcome message", "Hello! Welcome to my Photo Gallery!")
    
#창닫기
def close(event):
    window.destroy() 


##메인 코드
window=Tk()
window.geometry("520x500")
window.title("Photo Gallery")
window.resizable(False, False)
window.configure(background="white")

canvas = Canvas(window, width=450, height=300, bg="black")

window.bind("<Left>", pageLeft)
window.bind("<Right>", pageRight)
window.bind("<Escape>", close)

#타이틀
titleLabel = Label(window, text="Photo Gallery", font="Courier 20", bg="white")
titleLabel.bind("<Button-1>", clickClick)

#버튼생성
button1= Button(window, text="◀", bg="white", bd=0,relief="flat", font=20, command=clickPrev)
button2= Button(window, text="▶", bg="white", bd=0, relief="flat", font=20, command=clickNext)

#사진이름
text = Label(window, text=fnameList[0], bg="white", font="Courier 10")

#사진
photo = PhotoImage(file="gif/"+fnameList[0])
pLabel = Label(canvas, image = photo)


#위치
canvas.place(x=30, y=130) #캔버스
titleLabel.place(x=150, y=30) #타이틀
button1.place(x=220, y=460) #버튼1
button2.place(x=270, y=460) #버튼2
text.place(x=215, y = 435) #사진이름
pLabel.place(x=0, y=0) #사진


window.mainloop()



