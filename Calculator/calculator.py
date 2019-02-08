#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import Label

top = tkinter.Tk()
top.geometry('175x365')
top.title("Calculator")
w = Label(top, text="")
w.grid(row=0, column=0, columnspan=5,)




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
   w.config(text=w.cget("text")+"*")
def equalllback():
   w.config(text=str((eval(w.cget("text")))))
def divideCallback():
   mytext=w.cget("text")
   if mytext[-1:] in [".","*","//","-","+"]:
       print('operator already present')
   else:
       w.config(text=w.cget("text")+"//")
       
       
def clearCallback():
   w.config(text="")
def dotcallback():
   w.config(text=w.cget("text")+".")

B = tkinter.Button(top, text ="1", command = oneCallBack, height=4, width=4)
B2 = tkinter.Button(top, text ="2", command = twoCallBack, height=4, width=4)
B3 = tkinter.Button(top, text ="3", command = threeCallback, height=4, width=4)
B4 = tkinter.Button(top, text ="4", command = fourCallback, height=4, width=4)
B5 = tkinter.Button(top, text ="5", command = fiveCallback, height=4, width=4)
B6 = tkinter.Button(top, text ="6", command = sixCallback, height=4, width=4)
B7 = tkinter.Button(top, text ="7", command = sevenCallback, height=4, width=4)
B8 = tkinter.Button(top, text ="8", command = eightCallback, height=4, width=4)
B9 = tkinter.Button(top, text ="9", command = nineCallback, height=4, width=4)
BA = tkinter.Button(top, text ="+", command = AddCallback, height=4, width=4)
BS = tkinter.Button(top, text ="-", command = Subtractllback, height=4, width=4)
BM = tkinter.Button(top, text ="X", command = multiplyllback, height=4, width=4)
BD = tkinter.Button(top, text ="/", command = divideCallback, height=4, width=4)
B0 = tkinter.Button(top, text ="0", command = zeroCallback, height=4, width=4)
BC = tkinter.Button(top, text ="C", command = clearCallback, height=4, width=4)
BE = tkinter.Button(top, text ="=", command = equalllback, height=4, width=19)
Bdot = tkinter.Button(top, text =".", command = dotcallback, height=4, width=4)



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
BE.grid(row=5, column=0, columnspan=4)
B0.grid(row=4, column=0)
BD.grid(row=4, column=3)
BC.grid(row=4, column=2)
Bdot.grid(row=4, column=1)




top.mainloop()
