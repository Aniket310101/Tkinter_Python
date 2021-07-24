from tkinter import *
import tkinter.messagebox as tmsg

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i=0
root = Tk()
root.geometry("700x400")
root.title("List Box")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of ListBox")

Button(root, text="Add Item",command=add).pack()

root.mainloop()