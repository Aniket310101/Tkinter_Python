from tkinter import *
import time

root = Tk()

def upload():
    statusvar.set("Busy...")
    sbar.update()
    time.sleep(3)
    statusvar.set("Ready")


root.geometry("700x400")
root.title("Status Bar")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM,fill=X)

Button(root, text="Upload",command=upload).pack()

root.mainloop()