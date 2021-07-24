from tkinter import *

root = Tk()

root.geometry("900x900")
root.title("Frames")

f1 = Frame(root, bg="grey",borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey",borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)


l = Label(f1, text="Project Tkinter - PyCharm")
l.pack(pady=142)

l2 = Label(f2, text="Welcome to Text Editor", font="Helvetica 16 bold", fg="red", pady=22)
l2.pack()

root.mainloop()