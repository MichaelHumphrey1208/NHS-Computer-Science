import tkinter
top = tkinter.Tk()

top.geometry('260x390')
top.title("conect_four")
def colum1callback():
    print("yes")

def colum2callback():
    print("yes")
def colum3callback():
    print("yes")
def colum4callback():
    print("yes")
def colum5callback():
    print("yes")
def colum6callback():
    print("yes")
def colum7callback():
    print("yes")
Tc1 = tkinter.Button(top, text ="1", command = colum1callback, height=4, width=4)
Tc2 = tkinter.Button(top, text ="2", command = colum2callback, height=4, width=4)
Tc3 = tkinter.Button(top, text ="3", command = colum3callback, height=4, width=4)
Tc4 = tkinter.Button(top, text ="4", command = colum4callback, height=4, width=4)
Tc5 = tkinter.Button(top, text ="5", command = colum5callback, height=4, width=4)
Tc6 = tkinter.Button(top, text ="6", command = colum6callback, height=4, width=4)
Tc7 = tkinter.Button(top, text ="7", command = colum7callback, height=4, width=4)


Tc1.grid(row=0, column=0)
Tc2.grid(row=0, column=1)
Tc3.grid(row=0, column=2)
Tc4.grid(row=0, column=3)
Tc5.grid(row=0, column=4)
Tc6.grid(row=0, column=5)
Tc7.grid(row=0, column=6)

create_circle(100, 100, 20, myCanvas)
create_circle(50, 25, 10, myCanvas)

top.mainloop()


