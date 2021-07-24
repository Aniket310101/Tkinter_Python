from tkinter import *

root = Tk()
root.geometry("900x900")

def hello():
    print("WELCOME")

def name():
    print("Type your name")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Print now", command=name)
b2.pack(side=LEFT, padx=23)

root.mainloop()