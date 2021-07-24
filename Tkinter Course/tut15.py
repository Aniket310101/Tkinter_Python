from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def func():
    print("This is menu Bar!")

def help():
    print("What can I do for You?")
    tmsg.showinfo("INFO","What can I do for you?")

def rate():
    print("Rate Us")
    value = tmsg.askquestion("Rate","How was your experiance?")
    if value == "yes":
        msg = "Great!"
    else:
        msg = "Tell us what went wrong?"
    tmsg.showinfo("Experience", msg)

def fr():
    ans = tmsg.askretrycancel("Confirmation","Are You Sure?")
    if ans:
        print("No Problem")
    else:
        print("Befriending")

root.geometry("700x400")
root.title("Menus and Submenus")

# For dropdown menu bar
mymenu1 = Menu(root)

m1 = Menu(mymenu1, tearoff=0)
m1.add_command(label="Save", command=func)
m1.add_command(label="Save As", command=func)
m1.add_separator()
m1.add_command(label="New File", command=func)
m1.add_command(label="New Folder", command=func)
root.config(menu=mymenu1)
mymenu1.add_cascade(label="File",menu=m1)

m2 = Menu(mymenu1, tearoff=0)
m2.add_command(label="Save", command=func)
m2.add_command(label="Save As", command=func)
m2.add_separator()
m2.add_command(label="New File", command=func)
m2.add_command(label="New Folder", command=func)
root.config(menu=mymenu1)
mymenu1.add_cascade(label="Edit",menu=m1)

m3 = Menu(mymenu1, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate", command=rate)
m3.add_command(label="Befriend", command=fr)
root.config(menu=mymenu1)
mymenu1.add_cascade(label="Help",menu=m3)

root.mainloop()