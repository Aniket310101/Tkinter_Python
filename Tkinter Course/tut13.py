from tkinter import *

root = Tk()

def func(event):
    print(f"Clicked at {event.x}, {event.y}")
    # root.geometry("1000x1000")

root.geometry("600x400")
root.title("Events in tKinter")

widget = Button(root,text="Click me!")
widget.pack()

widget.bind('<Button-1>', func)
widget.bind('<Double-1>', quit)

root.mainloop()