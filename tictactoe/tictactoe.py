import tkinter
top = tkinter.Tk()

top.geometry('200x380')
top.title("two_tic_tac_toe")
turn="X"
def toggels():
    global turn
    if turn =="X":
        turn="O"
    else:
        turn= 'X'
def win():
   if bc1.cget('text') == 'X' and bc4.cget('text') == 'X' and bc7.cget('text') == 'X' and bc3.cget('text') == 'X' and bc6.cget('text') == 'X' and bc9.cget('text') == 'X' and bc2.cget('text') == 'X' and bc4.cget('text') == 'X',and b8.cget('text') == 'X'

def b1callback():
    global turn
    Bc1.configure(text=turn)
    toggels()
    win()
def b2callback():
    print("two")
    global turn
    Bc2.configure(text=turn)
    toggels()
def b3callback():
    print("two")
    global turn
    Bc3.configure(text=turn)
    toggels()
def b4callback():
    print("two")
    global turn
    Bc4.configure(text=turn)
    toggels()
def b5callback():
    print("two")
    global turn
    Bc5.configure(text=turn)
    toggels()
def b6callback():
    print("two")
    global turn
    Bc6.configure(text=turn)
    toggels()
def b7callback():
    print("two")
    global turn
    Bc7.configure(text=turn)
    toggels()
def b8callback():
    print("two")
    global turn
    Bc8.configure(text=turn)
    toggels()
def b9callback():
    print("two")
    global turn
    Bc9.configure(text=turn)
    toggels()

Bc1 = tkinter.Button(top, text ="1", command = b1callback, height=4, width=4)
Bc2 = tkinter.Button(top, text ="2", command = b2callback, height=4, width=4)
Bc3 = tkinter.Button(top, text ="3", command = b3callback, height=4, width=4)
Bc4 = tkinter.Button(top, text ="4", command = b4callback, height=4, width=4)
Bc5 = tkinter.Button(top, text ="5", command = b5callback, height=4, width=4)
Bc6 = tkinter.Button(top, text ="6", command = b6callback, height=4, width=4)
Bc7 = tkinter.Button(top, text ="7", command = b7callback, height=4, width=4)
Bc8 = tkinter.Button(top, text ="8", command = b8callback, height=4, width=4)
Bc9 = tkinter.Button(top, text ="9", command = b9callback, height=4, width=4)

Bc1.grid(row=1, column=0)
Bc2.grid(row=1, column=1)
Bc3.grid(row=1, column=2)
Bc4.grid(row=2, column=0)
Bc5.grid(row=2, column=1)
Bc6.grid(row=2, column=2)
Bc7.grid(row=3, column=0)
Bc8.grid(row=3, column=1)
Bc9.grid(row=3, column=2)



top.mainloop()

