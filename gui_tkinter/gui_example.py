from tkinter import *
import tkinter.ttk
from random import randint


def roll():
    n = str(randint(1, 6))
    result.configure(text=n)


top = Tk()

roll_button = Button(top, text='Roll', command=roll)
result = Label(top, width=200)

roll_button.grid(row=0)
result.grid(row=1)
