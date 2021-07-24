from tkinter import *

root = Tk()

#HeightXWidth
root.geometry("455x244")

# width, height
root.minsize(300,100)

# width, height
root.maxsize(1200,988)

#label
lb = Label(text="My First GUI")
lb.pack()

root.mainloop()