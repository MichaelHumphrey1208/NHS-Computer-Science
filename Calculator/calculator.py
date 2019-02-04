#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import Label

top = tkinter.Tk()
top.geometry('450x2000')
top.title("Calculator")
w = Label(top, text="")
w.grid(row=0, column=0)




def oneCallBack():
   w.config(text=w.cget("text")+"1")

def twoCallBack():
   w.config(text=w.cget("text")+"2")
def threeCallback():
   w.config(text=w.cget("text")+"3")
def fourCallback():
   w.config(text=w.cget("text")+"4")
def fiveCallback():
   w.config(text=w.cget("text")+"5")
def sixCallback():
   w.config(text=w.cget("text")+"6")
def sevenCallback():
   w.config(text=w.cget("text")+"7")
def eightCallback():
   w.config(text=w.cget("text")+"8")
def nineCallback():
   w.config(text=w.cget("text")+"9")
def zeroCallback():
   w.config(text=w.cget("text")+"0")
def AddCallback():
   w.config(text=w.cget("text")+"+")
def Subtractllback():
   w.config(text=w.cget("text")+"-")
def multiplyllback():
   w.config(text=w.cget("text")+"X")
def equalllback():
   w.config(text=(eval(w.cget("text"))))
def divideCallback():
   w.config(text=w.cget("text")+"")
def clearCallback():
   w.config(text="")

B = tkinter.Button(top, text ="1", command = oneCallBack)
B2 = tkinter.Button(top, text ="2", command = twoCallBack)
B3 = tkinter.Button(top, text ="3", command = threeCallback)
B4 = tkinter.Button(top, text ="4", command = fourCallback)
B5 = tkinter.Button(top, text ="5", command = fiveCallback)
B6 = tkinter.Button(top, text ="6", command = sixCallback)
B7 = tkinter.Button(top, text ="7", command = sevenCallback)
B8 = tkinter.Button(top, text ="8", command = eightCallback)
B9 = tkinter.Button(top, text ="9", command = nineCallback)
BA = tkinter.Button(top, text ="+", command = AddCallback)
BS = tkinter.Button(top, text ="-", command = Subtractllback)
BM = tkinter.Button(top, text ="X", command = multiplyllback)
BE = tkinter.Button(top, text ="=", command = equalllback)
B0 = tkinter.Button(top, text ="0", command = zeroCallback)
BD = tkinter.Button(top, text ="/", command = divideCallback)
BC = tkinter.Button(top, text ="C", command = clearCallback)


B.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)
B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)
B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)
BA.grid(row=1, column=3)
BS.grid(row=2, column=3)
BM.grid(row=3, column=3)
BE.grid(row=4, column=3)
B0.grid(row=4, column=0)
BD.grid(row=4, column=1)
BC.grid(row=4, column=2)



top.mainloop()
