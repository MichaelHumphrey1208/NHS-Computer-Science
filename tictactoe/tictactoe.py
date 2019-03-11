import tkinter
import random
top = tkinter.Tk()

top.geometry('200x380')
top.title("two_tic_tac_toe")
turn="X"
def clearing():
    Bc1.configure(text=' ')
    Bc2.configure(text=' ')
    Bc3.configure(text=' ')
    Bc4.configure(text=' ')
    Bc5.configure(text=' ')
    Bc6.configure(text=' ')
    Bc7.configure(text=' ')
    Bc8.configure(text=' ')
    Bc9.configure(text=' ')
def Rnm():
    while True:
        value =random.randint(1,9)
         if value == 1:
             if Bc1.cget('text') == 'x' or Bc1.cget('text') == 'O'
                break
         else:
            Bc1.cget('text') == 'O'   
Won= False
def toggels():
    global turn
    if turn =="X":
        turn="O"
    else:
        turn= 'X'
def win():
   global Won
   if Bc1.cget('text') == 'X' and Bc4.cget('text') == 'X' and Bc7.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc2.cget('text') == 'X' and Bc5.cget('text') == 'X' and Bc8.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc3.cget('text') == 'X' and Bc6.cget('text') == 'X' and Bc9.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc1.cget('text') == 'X' and Bc5.cget('text') == 'X' and Bc9.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc1.cget('text') == 'X' and Bc2.cget('text') == 'X' and Bc3.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc4.cget('text') == 'X' and Bc5.cget('text') == 'X' and Bc6.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc7.cget('text') == 'X' and Bc8.cget('text') == 'X' and Bc9.cget('text') == 'X':
       print("you win")
       Won=True
   if Bc3.cget('text') == 'X' and Bc5.cget('text') == 'X' and Bc7.cget('text') == 'X':
       print("you win")
       #clearing()
       Won=True
   if Bc1.cget('text') == 'O' and Bc4.cget('text') == 'O' and Bc7.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc2.cget('text') == 'O' and Bc5.cget('text') == 'O' and Bc8.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc3.cget('text') == 'O' and Bc6.cget('text') == 'O' and Bc9.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc1.cget('text') == 'O' and Bc5.cget('text') == 'O' and Bc9.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc1.cget('text') == 'O' and Bc2.cget('text') == 'O' and Bc3.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc4.cget('text') == 'O' and Bc5.cget('text') == 'O' and Bc6.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc7.cget('text') == 'O' and Bc8.cget('text') == 'O' and Bc9.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
   if Bc3.cget('text') == 'O' and Bc5.cget('text') == 'O' and Bc7.cget('text') == 'O':
       print("you win")
       #clearing()
       Won=True
def b1callback():
    global turn
    global Won
    if not Won:
        Bc1.configure(text=turn)
        toggels()
        win()
    Rnm()
def b2callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc2.configure(text=turn)
        toggels()
        win()
def b3callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc3.configure(text=turn)
        toggels()
        win()
def b4callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc4.configure(text=turn)
        toggels()
        win()
def b5callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc5.configure(text=turn)
        toggels()
        win()
def b6callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc6.configure(text=turn)
        toggels()
        win()
def b7callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc7.configure(text=turn)
        toggels()
        win()
def b8callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc8.configure(text=turn)
        toggels()
        win()
def b9callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc9.configure(text=turn)
        toggels()
        win()
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

