from tkinter import *

root = Tk()

def func():
    print("This is menu Bar!")

root.geometry("700x400")
root.title("Menus and Submenus")

# # For non dropdown menu bar
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=func)
# mymenu.add_command(label="Quit", command=exit)
# root.config(menu=mymenu)

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

root.mainloop()