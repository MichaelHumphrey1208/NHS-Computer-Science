import tkinter
import random
top = tkinter.Tk()

top.geometry('260x390')
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
def ComputerM():
    if computer== True:
        while True:
            value =random.randint(1,9)
            if value == 1:
                if Bc1.cget('text') == 'X' or Bc1.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc1.config(text="O")
                    break
            if value == 2:
                if Bc2.cget('text') == 'X' or Bc2.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc2.config(text="O")
                    break
            if value == 3:
                if Bc3.cget('text') == 'X' or Bc3.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc3.config(text="O")
                    break
            if value == 4:
                if Bc4.cget('text') == 'X' or Bc4.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc4.config(text="O")
                    break
            if value == 5:
                if Bc5.cget('text') == 'X' or Bc5.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc5.config(text="O")
                    break
            if value == 6:
                if Bc6.cget('text') == 'X' or Bc6.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc6.config(text="O")
                    break
            if value == 7:
                if Bc7.cget('text') == 'X' or Bc7.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc7.config(text="O")
                    break
            if value == 8:
                if Bc8.cget('text') == 'X' or Bc8.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc8.config(text="O")
                    break
            if value == 9:
                if Bc9.cget('text') == 'X' or Bc9.cget('text') == 'O':
                    continue
                else:
                    toggelsCom()
                    Bc9.config(text="O")
                    break
        
Won= False
def toggels():
    if multiP== True:
        global turn
        if turn =="X":
            turn="O"
        else:
            turn= 'X'
def toggelsCom():
    if computer== True:
        global turn
         
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
computer= False
def compcallback():
    print("zero")
    global computer
    if computer == False:
        computer=True
    else:
        computer=False
def clearcallback():
    clearing()
    print("new game")
multiP=False
def multiplayercallback():
    print("two players")
    global multiP
    if multiP == False:
        multiP=True
    else:
        multiP=False
def b1callback():
    global turn
    global Won
    if not Won:
        Bc1.configure(text=turn)
    win()
    ComputerM()
    toggels()
def b2callback():
    print("two")
    global turn
    global Won
    if not Won:
        Bc2.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
def b3callback():
    print("three")
    global turn
    global Won
    if not Won:
        Bc3.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
    win()
def b4callback():
    print("four")
    global turn
    global Won
    if not Won:
        Bc4.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
def b5callback():
    print("five")
    global turn
    global Won
    if not Won:
        Bc5.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
def b6callback():
    print("six")
    global turn
    global Won
    if not Won:
        Bc6.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
def b7callback():
    print("seven")
    global turn
    global Won
    if not Won:
        Bc7.configure(text=turn)
    win()
    if not Won:
        ComputerM()
    toggels()
def b8callback():
    print("eight")
    global turn
    global Won
    if not Won:
        Bc8.configure(text=turn)
    win()
    if not Won:
      ComputerM()
    toggels()
def b9callback():
    print("ninne")
    global turn
    global Won
    if not Won:
        Bc9.configure(text=turn)
    toggels()
    win()
    if not Won:
        ComputerM()
    toggels()

Bclm = tkinter.Button(top, text ="clear", command = clearcallback, height=4, width=9)
Bcm = tkinter.Button(top, text ="2players", command = multiplayercallback, height=4, width=9)
Bc1 = tkinter.Button(top, text ="1", command = b1callback, height=4, width=9)
Bc2 = tkinter.Button(top, text ="2", command = b2callback, height=4, width=9)
Bc3 = tkinter.Button(top, text ="3", command = b3callback, height=4, width=9)
Bc4 = tkinter.Button(top, text ="4", command = b4callback, height=4, width=9)
Bc5 = tkinter.Button(top, text ="5", command = b5callback, height=4, width=9)
Bc6 = tkinter.Button(top, text ="6", command = b6callback, height=4, width=9)
Bc7 = tkinter.Button(top, text ="7", command = b7callback, height=4, width=9)
Bc8 = tkinter.Button(top, text ="8", command = b8callback, height=4, width=9)
Bc9 = tkinter.Button(top, text ="9", command = b9callback, height=4, width=9)
Bc0 = tkinter.Button(top, text ="singel player", command = compcallback, height=4, width=9,)

Bclm.grid(row=0, column=1, columnspan=1)
Bcm.grid(row=0, column=2, columnspan=1)
Bc0.grid(row=0, column=0, columnspan=1)
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

