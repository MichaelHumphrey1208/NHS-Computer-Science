#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox

top = tkinter.Tk()
top.geometry('450x2000')
top.title("Calculator")
lbl = Label(top, text="Hello")
 
lbl.grid(column=0, row=0)

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
