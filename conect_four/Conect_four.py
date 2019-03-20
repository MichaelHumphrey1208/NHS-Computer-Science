import tkinter
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=700, width=700)
top.geometry('2000x3000')
top.title("conect_four_board")

#                    X   y   x   y
Row1C1 = C.create_oval(45, 25, 85, 65, fill="white")
Row1C2 = C.create_oval(145, 25, 185, 65, fill="white")
Row1C3 = C.create_oval(245, 25, 285, 65, fill="white")
Row1C4 = C.create_oval(345, 25, 385, 65, fill="white")
Row1C5 = C.create_oval(445, 25, 485, 65, fill="white")
Row1C6 = C.create_oval(545, 25, 585, 65, fill="white")
row1C7 = C.create_oval(645, 25, 685, 65, fill="white")


Row2C1 = C.create_oval(45, 125, 85, 165, fill="white")
Row2C2 = C.create_oval(145, 125, 185, 165, fill="white")
Row2C3 = C.create_oval(245, 125, 285, 165, fill="white")
Row2C4 = C.create_oval(345, 125, 385, 165, fill="white")
Row2C5 = C.create_oval(445, 125, 485, 165, fill="white")
Row2C6 = C.create_oval(545, 125, 585, 165, fill="white")
row2C7 = C.create_oval(645, 125, 685, 165, fill="white")


row3c1 = C.create_oval(45, 225, 85, 265, fill="white")
row3c2 = C.create_oval(145, 225, 185, 265, fill="white")
row3c3 = C.create_oval(245, 225, 285, 265, fill="white")
row3c4 = C.create_oval(345, 225, 385, 265, fill="white")
row3c5 = C.create_oval(445, 225, 485, 265, fill="white")
row3c6 = C.create_oval(545, 225, 585, 265, fill="white")
row3C7 = C.create_oval(645, 225, 685, 265, fill="white")


row4C1 = C.create_oval(45, 325, 85, 365, fill="white")
row4C2 = C.create_oval(145, 325, 185, 365, fill="white")
row4C3 = C.create_oval(245, 325, 285, 365, fill="white")
row4C4 = C.create_oval(345, 325, 385, 365, fill="white")
row4C5 = C.create_oval(445, 325, 485, 365, fill="white")
row4C6 = C.create_oval(545, 325, 585, 365, fill="white")
row4C7 = C.create_oval(645, 325, 685, 365, fill="white")


row5c1 = C.create_oval(45, 425, 85, 465, fill="white")
row5c2 = C.create_oval(145, 425, 185, 465, fill="white")
row5c3 = C.create_oval(245, 425, 285, 465, fill="white")
row5c4 = C.create_oval(345, 425, 385, 465, fill="white")
row5c5 = C.create_oval(445, 425, 485, 465, fill="white")
row5c6 = C.create_oval(545, 425, 585, 465, fill="white")
row5c7 = C.create_oval(645, 425, 685, 465, fill="white")

row6c1 = C.create_oval(45, 525, 85, 565, fill="white")
row6c2 = C.create_oval(145, 525, 185, 565, fill="white")
row6c3 = C.create_oval(245, 525, 285, 565, fill="white")
row6c4 = C.create_oval(345, 525, 385, 565, fill="white")
row6c5 = C.create_oval(445, 525, 485, 565, fill="white")
row6c6 = C.create_oval(545, 525, 585, 565, fill="white")
row6c7 = C.create_oval(645, 525, 685, 565, fill="white")

def c1callback():
    print("c1")
def c2callback():
    print("c1")
def c3callback():
    print("c1")
def c4callback():
    print("c1")
def c5callback():
    print("c1")
def c6callback():
    print("c1")
def c7callback():
    print("c1")
    
Tc1 = tkinter.Button(top, text ="1", command = c1callback, height=4, width=4)
Tc2 = tkinter.Button(top, text ="2", command = c2callback, height=4, width=4)
Tc3 = tkinter.Button(top, text ="3", command = c3callback, height=4, width=4)
Tc4 = tkinter.Button(top, text ="4", command = c4callback, height=4, width=4)
Tc5 = tkinter.Button(top, text ="5", command = c5callback, height=4, width=4)
Tc6 = tkinter.Button(top, text ="6", command = c6callback, height=4, width=4)
Tc7 = tkinter.Button(top, text ="7", command = c7callback, height=4, width=4)

Tc1.place(y=35, x=150)
Tc2.place(y=35, x=250)
Tc3.place(y=35, x=350)
Tc4.place(y=35, x=450)
Tc5.place(y=35, x=550)
Tc6.place(y=35, x=650)
Tc7.place(y=35, x=750)



C.place(x=100, y=100)
top.mainloop()

