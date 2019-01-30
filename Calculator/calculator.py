#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import Label

top = tkinter.Tk()
top.geometry('450x2000')
top.title("Calculator")
w = Label(top, text="Hello")
w.grid(row=0, column=0)
a = Label(top, text="one")
a.grid(row=0, column=1)
def helloCallBack():
   a.config(text="2")

def hello2CallBack():
   w.config(text="1")

B = tkinter.Button(top, text ="2", command = helloCallBack)
B2 = tkinter.Button(top, text ="1", command = hello2CallBack)


B.grid(row=1, column=0)
B2.grid(row=1, column=1)
top.mainloop()
