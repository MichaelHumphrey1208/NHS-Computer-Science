import tkinter

top = tkinter.Tk()

top.geometry('175x365')
top.title("lights out")
def oneCallback():
    print("one!")
def twoCallback():
    print("two!")
def threeCallback():
    print("mabey!")
def fourCallback():
    print("!")
def fiveCallback():
    print("5")
    print(B5)
    B5.configure(background = "red")
def sixCallback():
    print("!")
def sevenCallback():
    print("!")
def eightCallback():
    print("!")
def nineCallback():
    print("!")
def tenCallback():
    print("!")
def elevenCallback():
    print("!")
def tweleveCallback():
    print("!")
def thrirteenCallback():
    print("!")
def fourteenCallback():
    print("!")
def fifteenCallback():
    print("!")
def sixteenCallback():
    print("!")
B1 = tkinter.Button(top, text ="1", command = oneCallback, height=4, width=4)
B2 = tkinter.Button(top, text ="2", command = twoCallback, height=4, width=4)
B3 = tkinter.Button(top, text ="3", command = threeCallback, height=4, width=4)
B4 = tkinter.Button(top, text ="4", command = fourCallback, height=4, width=4)
B5 = tkinter.Button( top, bg="blue", text ="5",command = fiveCallback, height=4, width=4)
B6 = tkinter.Button(top, text ="6", command = sixCallback, height=4, width=4)
B7 = tkinter.Button(top, text ="7", command = sevenCallback, height=4, width=4)
B8 = tkinter.Button(top, text ="8", command = eightCallback, height=4, width=4)
B9 = tkinter.Button(top, text ="9", command = nineCallback, height=4, width=4)
B10 = tkinter.Button(top, text ="10", command = tenCallback, height=4, width=4)
B11 = tkinter.Button(top, text ="11", command = elevenCallback, height=4, width=4)
B12 = tkinter.Button(top, text ="12", command = tweleveCallback, height=4, width=4)
B13 = tkinter.Button(top, text ="13", command = thrirteenCallback, height=4, width=4)
B14 = tkinter.Button(top, text ="14", command = fourteenCallback, height=4, width=4)
B15 = tkinter.Button(top, text ="15", command = fifteenCallback, height=4, width=4)
B16 = tkinter.Button(top, text ="16", command = sixteenCallback, height=4, width=4)


B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)
B4.grid(row=1, column=3)
B5.grid(row=2, column=0)
B6.grid(row=2, column=1)
B7.grid(row=2, column=2)
B8.grid(row=2, column=3)
B9.grid(row=3, column=0)
B10.grid(row=3, column=1)
B11.grid(row=3, column=2)
B12.grid(row=3, column=3)
B13.grid(row=4, column=0)
B14.grid(row=4, column=1)
B15.grid(row=4, column=2)
B16.grid(row=4, column=3)




top.mainloop()


