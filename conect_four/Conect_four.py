import tkinter
import random
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=600, width=700)
top.geometry('2000x3000')
top.title("conect_four_board")
colm1 = ["white", "white", "white", "white", "white", "white",]
colm2 = ["white", "white", "white", "white", "white", "white",]
colm2 = ["white", "white", "white", "white", "white", "white",]
colm3 = ["white", "white", "white", "white", "white", "white",]
colm4 = ["white", "white", "white", "white", "white", "white",]
colm5 = ["white", "white", "white", "white", "white", "white",]
colm6 = ["white", "white", "white", "white", "white", "white",]
colm7 = ["white", "white", "white", "white", "white", "white",]


def board():
       #                    X   y   x   y
    Row1c1 = C.create_oval(45, 25, 85, 65, fill=colm1[0])
    Row1c2 = C.create_oval(145, 25, 185, 65, fill=colm2[0])
    Row1c3 = C.create_oval(245, 25, 285, 65, fill=colm3[0])
    Row1c4 = C.create_oval(345, 25, 385, 65, fill=colm4[0])
    Row1c5 = C.create_oval(445, 25, 485, 65, fill=colm5[0])
    Row1c6 = C.create_oval(545, 25, 585, 65, fill=colm6[0])
    row1c7 = C.create_oval(645, 25, 685, 65, fill=colm7[0])


    Row2c1 = C.create_oval(45, 125, 85, 165, fill=colm1[1])
    Row2c2 = C.create_oval(145, 125, 185, 165, fill=colm2[1])
    Row2c3 = C.create_oval(245, 125, 285, 165, fill=colm3[1])
    Row2c4 = C.create_oval(345, 125, 385, 165, fill=colm4[1])
    Row2c5 = C.create_oval(445, 125, 485, 165, fill=colm5[1])
    Row2c6 = C.create_oval(545, 125, 585, 165, fill=colm6[1])
    row2c7 = C.create_oval(645, 125, 685, 165, fill=colm7[1])


    row3c1 = C.create_oval(45, 225, 85, 265, fill=colm1[2])
    row3c2 = C.create_oval(145, 225, 185, 265, fill=colm2[2])
    row3c3 = C.create_oval(245, 225, 285, 265, fill=colm3[2])
    row3c4 = C.create_oval(345, 225, 385, 265, fill=colm4[2])
    row3c5 = C.create_oval(445, 225, 485, 265, fill=colm5[2])
    row3c6 = C.create_oval(545, 225, 585, 265, fill=colm6[2])
    row3c7 = C.create_oval(645, 225, 685, 265, fill=colm7[2])


    row4c1 = C.create_oval(45, 325, 85, 365, fill=colm1[3])
    row4c2 = C.create_oval(145, 325, 185, 365, fill=colm2[3])
    row4c3 = C.create_oval(245, 325, 285, 365, fill=colm3[3])
    row4c4 = C.create_oval(345, 325, 385, 365, fill=colm4[3])
    row4c5 = C.create_oval(445, 325, 485, 365, fill=colm5[3])
    row4c6 = C.create_oval(545, 325, 585, 365, fill=colm6[3])
    row4c7 = C.create_oval(645, 325, 685, 365, fill=colm7[3])


    row5c1 = C.create_oval(45, 425, 85, 465, fill=colm1[4])
    row5c2 = C.create_oval(145, 425, 185, 465, fill=colm2[4])
    row5c3 = C.create_oval(245, 425, 285, 465, fill=colm3[4])
    row5c4 = C.create_oval(345, 425, 385, 465, fill=colm4[4])
    row5c5 = C.create_oval(445, 425, 485, 465, fill=colm5[4])
    row5c6 = C.create_oval(545, 425, 585, 465, fill=colm6[4])
    row5c7 = C.create_oval(645, 425, 685, 465, fill=colm7[4])

    row6c1 = C.create_oval(45, 525, 85, 565, fill=colm1[5])
    row6c2 = C.create_oval(145, 525, 185, 565, fill=colm2[5])
    row6c3 = C.create_oval(245, 525, 285, 565, fill=colm3[5])
    row6c4 = C.create_oval(345, 525, 385, 565, fill=colm4[5])
    row6c5 = C.create_oval(445, 525, 485, 565, fill=colm5[5])
    row6c6 = C.create_oval(545, 525, 585, 565, fill=colm6[5])
    row6c7 = C.create_oval(645, 525, 685, 565, fill=colm7[5])
board()
turn ="red"
def turns():
    global turn
    if turn == "red":
        turn = "yellow"
    else:
        if turn == "yellow":
            turn = "red"
computer= False
def c1callback():
    turns()
    if colm1[5] == "white":
        colm1[5] = turn
        print(colm1[5])
        print(turn)
        board()
    elif colm1[4] == "white":
            colm1[4] = turn
            print(colm1[4])
            board()
            print(turn)
    elif colm1[3] == "white":
            colm1[3] = turn
            print(colm1[3])
            board()
            print(turn)
    elif colm1[2] == "white":
            colm1[2] = turn
            print(colm1[2])
            board()
            print(turn)
    elif colm1[1] == "white":
            colm1[1] = turn
            print(colm1[1])
            board()
            print(turn)
    elif colm1[0] == "white":
            colm1[0] = turn
            print(colm1[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c2callback():
    turns()
    if colm2[5] == "white":
        colm2[5] = turn
        print(colm2[5])
        print(turn)
        board()
    elif colm2[4] == "white":
            colm2[4] = turn
            print(colm2[4])
            board()
            print(turn)
    elif colm2[3] == "white":
            colm2[3] = turn
            print(colm2[3])
            board()
            print(turn)
    elif colm2[2] == "white":
            colm2[2] = turn
            print(colm2[2])
            board()
            print(turn)
    elif colm2[1] == "white":
            colm2[1] = turn
            print(colm2[1])
            board()
            print(turn)
    elif colm2[0] == "white":
            colm2[0] = turn
            print(colm2[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c3callback():
    turns()
    if colm3[5] == "white":
        colm3[5] = turn
        print(colm3[5])
        board()
    elif colm3[4] == "white":
            colm3[4] = turn
            print(colm3[4])
            board()
            print(turn)
    elif colm3[3] == "white":
            colm3[3] = turn
            print(colm3[3])
            board()
            print(turn)
    elif colm3[2] == "white":
            colm3[2] = turn
            print(colm3[2])
            board()
            print(turn)
    elif colm3[1] == "white":
            colm3[1] = turn
            print(colm3[1])
            board()
            print(turn)
    elif colm3[0] == "white":
            colm3[0] = turn
            print(colm3[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c4callback():
    turns()
    if colm4[5] == "white":
        colm4[5] = turn
        print(colm4[5])
        board()
    elif colm4[4] == "white":
            colm4[4] = turn
            print(colm4[4])
            board()
            print(turn)
    elif colm4[3] == "white":
            colm4[3] = turn
            print(colm4[3])
            board()
            print(turn)
    elif colm4[2] == "white":
            colm4[2] = turn
            print(colm4[2])
            board()
            print(turn)
    elif colm4[1] == "white":
            colm4[1] = turn
            print(colm4[1])
            board()
            print(turn)
    elif colm4[0] == "white":
            colm4[0] = turn
            print(colm4[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c5callback():
    turns()
    if colm5[5] == "white":
        colm5[5] = turn
        print(colm5[5])
        board()
    elif colm5[4] == "white":
            colm5[4] = turn
            print(colm5[4])
            board()
            print(turn)
    elif colm5[3] == "white":
            colm5[3] = turn
            print(colm5[3])
            board()
            print(turn)
    elif colm5[2] == "white":
            colm5[2] = turn
            print(colm5[2])
            board()
            print(turn)
    elif colm5[1] == "white":
            colm5[1] = turn
            print(colm5[1])
            board()
            print(turn)
    elif colm5[0] == "white":
            colm5[0] = turn
            print(colm5[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c6callback():
    turns()
    if colm6[5] == "white":
        colm6[5] = turn
        print(colm6[5])
        board()
    elif colm6[4] == "white":
            colm6[4] = turn
            print(colm6[4])
            board()
            print(turn)
    elif colm6[3] == "white":
            colm6[3] = turn
            print(colm6[3])
            board()
            print(turn)
    elif colm6[2] == "white":
            colm6[2] = turn
            print(colm6[2])
            board()
            print(turn)
    elif colm6[1] == "white":
            colm6[1] = turn
            print(colm6[1])
            board()
            print(turn)
    elif colm6[0] == "white":
            colm6[0] = turn
            print(colm6[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
def c7callback():
    turns()
    if colm7[5] == "white":
        colm7[5] = turn
        print(colm7[5])
        board()
    elif colm7[4] == "white":
            colm7[4] = turn
            print(colm7[4])
            board()
            print(turn)
    elif colm7[3] == "white":
            colm7[3] = turn
            print(colm7[3])
            board()
            print(turn)
    elif colm7[2] == "white":
            colm7[2] = turn
            print(colm7[2])
            board()
            print(turn)
    elif colm7[1] == "white":
            colm7[1] = turn
            print(colm7[1])
            board()
            print(turn)
    elif colm7[0] == "white":
            colm7[0] = turn
            print(colm7[0])
            board()
            print(turn)
    else:
        turns()
    if computer == True:
        comcallback()
#cumputers functions
def cc1call():
    turns()
    if colm1[5] == "white":
        colm1[5] = turn
        print(colm1[5])
        print(turn)
        board()
    elif colm1[4] == "white":
            colm1[4] = turn
            print(colm1[4])
            board()
            print(turn)
    elif colm1[3] == "white":
            colm1[3] = turn
            print(colm1[3])
            board()
            print(turn)
    elif colm1[2] == "white":
            colm1[2] = turn
            print(colm1[2])
            board()
            print(turn)
    elif colm1[1] == "white":
            colm1[1] = turn
            print(colm1[1])
            board()
            print(turn)
    elif colm1[0] == "white":
            colm1[0] = turn
            print(colm1[0])
            board()
            print(turn)
    else:
        turns()
def cc2call():
    turns()
    if colm2[5] == "white":
        colm2[5] = turn
        print(colm2[5])
        print(turn)
        board()
    elif colm2[4] == "white":
            colm2[4] = turn
            print(colm2[4])
            board()
            print(turn)
    elif colm2[3] == "white":
            colm2[3] = turn
            print(colm2[3])
            board()
            print(turn)
    elif colm2[2] == "white":
            colm2[2] = turn
            print(colm2[2])
            board()
            print(turn)
    elif colm2[1] == "white":
            colm2[1] = turn
            print(colm2[1])
            board()
            print(turn)
    elif colm2[0] == "white":
            colm2[0] = turn
            print(colm2[0])
            board()
            print(turn)
    else:
        turns()
def cc3call():
    turns()
    if colm3[5] == "white":
        colm3[5] = turn
        print(colm3[5])
        board()
    elif colm3[4] == "white":
            colm3[4] = turn
            print(colm3[4])
            board()
            print(turn)
    elif colm3[3] == "white":
            colm3[3] = turn
            print(colm3[3])
            board()
            print(turn)
    elif colm3[2] == "white":
            colm3[2] = turn
            print(colm3[2])
            board()
            print(turn)
    elif colm3[1] == "white":
            colm3[1] = turn
            print(colm3[1])
            board()
            print(turn)
    elif colm3[0] == "white":
            colm3[0] = turn
            print(colm3[0])
            board()
            print(turn)
    else:
        turns()
def cc4call():
    turns()
    if colm4[5] == "white":
        colm4[5] = turn
        print(colm4[5])
        board()
    elif colm4[4] == "white":
            colm4[4] = turn
            print(colm4[4])
            board()
            print(turn)
    elif colm4[3] == "white":
            colm4[3] = turn
            print(colm4[3])
            board()
            print(turn)
    elif colm4[2] == "white":
            colm4[2] = turn
            print(colm4[2])
            board()
            print(turn)
    elif colm4[1] == "white":
            colm4[1] = turn
            print(colm4[1])
            board()
            print(turn)
    elif colm4[0] == "white":
            colm4[0] = turn
            print(colm4[0])
            board()
            print(turn)
    else:
        turns()
def cc5call():
    turns()
    if colm5[5] == "white":
        colm5[5] = turn
        print(colm5[5])
        board()
    elif colm5[4] == "white":
            colm5[4] = turn
            print(colm5[4])
            board()
            print(turn)
    elif colm5[3] == "white":
            colm5[3] = turn
            print(colm5[3])
            board()
            print(turn)
    elif colm5[2] == "white":
            colm5[2] = turn
            print(colm5[2])
            board()
            print(turn)
    elif colm5[1] == "white":
            colm5[1] = turn
            print(colm5[1])
            board()
            print(turn)
    elif colm5[0] == "white":
            colm5[0] = turn
            print(colm5[0])
            board()
            print(turn)
    else:
        turns()
def cc6call():
    turns()
    if colm6[5] == "white":
        colm6[5] = turn
        print(colm6[5])
        board()
    elif colm6[4] == "white":
            colm6[4] = turn
            print(colm6[4])
            board()
            print(turn)
    elif colm6[3] == "white":
            colm6[3] = turn
            print(colm6[3])
            board()
            print(turn)
    elif colm6[2] == "white":
            colm6[2] = turn
            print(colm6[2])
            board()
            print(turn)
    elif colm6[1] == "white":
            colm6[1] = turn
            print(colm6[1])
            board()
            print(turn)
    elif colm6[0] == "white":
            colm6[0] = turn
            print(colm6[0])
            board()
            print(turn)
    else:
        turns()
def cc7call():
    turns()
    if colm7[5] == "white":
        colm7[5] = turn
        print(colm7[5])
        board()
    elif colm7[4] == "white":
            colm7[4] = turn
            print(colm7[4])
            board()
            print(turn)
    elif colm7[3] == "white":
            colm7[3] = turn
            print(colm7[3])
            board()
            print(turn)
    elif colm7[2] == "white":
            colm7[2] = turn
            print(colm7[2])
            board()
            print(turn)
    elif colm7[1] == "white":
            colm7[1] = turn
            print(colm7[1])
            board()
            print(turn)
    elif colm7[0] == "white":
            colm7[0] = turn
            print(colm7[0])
            board()
            print(turn)
    else:
        turns()
def comcallback():
    global computer
    computer= True
    if computer == True:
        value =random.randint(1,7)
        if value ==1:
            cc1call()
            print("computer")
        elif value ==2:
            cc2call()
        elif value ==3:
            cc3call()
        elif value ==4:
            cc4call()
        elif value ==5:
            cc5call()
        elif value ==6:
            cc6call()
        else:
            value ==7
            cc7call()
CM = tkinter.Button(top, text ="PVC", command = comcallback, height=4, width=11)
Tc1 = tkinter.Button(top, text ="1", command = c1callback, height=4, width=11)
Tc2 = tkinter.Button(top, text ="2", command = c2callback, height=4, width=11)
Tc3 = tkinter.Button(top, text ="3", command = c3callback, height=4, width=11)
Tc4 = tkinter.Button(top, text ="4", command = c4callback, height=4, width=11)
Tc5 = tkinter.Button(top, text ="5", command = c5callback, height=4, width=11)
Tc6 = tkinter.Button(top, text ="6", command = c6callback, height=4, width=11)
Tc7 = tkinter.Button(top, text ="7", command = c7callback, height=4, width=11)

CM.place(y=35, x=1)
Tc1.place(y=35, x=101)
Tc2.place(y=35, x=201)
Tc3.place(y=35, x=301)
Tc4.place(y=35, x=401)
Tc5.place(y=35, x=501)
Tc6.place(y=35, x=601)
Tc7.place(y=35, x=701)



C.place(x=100, y=100)
top.mainloop()
