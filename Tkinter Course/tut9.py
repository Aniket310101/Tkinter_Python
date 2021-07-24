# GRID LAYOUT
from tkinter import *

def getvals():
    print(uservalue.get())
    print(passvalue.get())

root = Tk()
root.geometry("900x900")

user = Label(root, text="Username")
password= Label(root, text="Password")

user.grid()
password.grid(row=1)

# Variable Classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()