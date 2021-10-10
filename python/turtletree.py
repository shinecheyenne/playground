##Recursive Tree##
#python 3.9.6

import turtle
from random import randint

turtle.title("Recursive Tree")
myTree = turtle.Turtle()
myTree.hideturtle()

#function
def drawTree(length, num, base, angle):      
    if length > base:
        myTree.forward(length)
        myTree.left(angle)
        drawTree(length-num, num, base, angle)
        myTree.right(angle*2)
        drawTree(length-num, num, base, angle)

        color = ['lightpink', 'yellow', 'red', 'blue', 'purple', 'green']
        dotcolor = color[randint(0,len(color)-1)]
        myTree.fillcolor(dotcolor)
        myTree.begin_fill(); myTree.circle(2); myTree.end_fill()
        myTree.left(angle)
        myTree.backward(length)

def myText(text, color, font, size, sety):
    myTree.penup()
    myTree.sety(sety)
    myTree.color(color)
    myTree.write(text, False, align='center', font=(font,size,'normal'))


#main code
###color setup
colors = ['paleturquoise','azure','honeydew','powderblue','lightcyan','snow', 'lavender']
for i in range(0, len(colors)):
    myTree.hideturtle()
    myTree.speed(0)
    myTree.color(colors[i])
    myTree.setheading(90 + 360/len(colors)*i)
    ### Tree setup(initial length, subtrahend, unit length, angle)
    drawTree(50, 7, 15, 30)
###text setup(text, color, font, size)    
myText("Recursive Tree", "lightgrey", "Times New Roman", 18, -250)
myText("cheyenne", "lightgrey", "Times New Roman", 15, -270)
turtle.exitonclick()
