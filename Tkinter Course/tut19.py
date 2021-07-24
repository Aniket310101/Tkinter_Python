from tkinter import *
import tkinter.messagebox as tmsg

i=0
root = Tk()
root.geometry("700x400")
root.title("ScrollBar")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(344):
    listbox.insert(END, f"Item {i}")

listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)

root.mainloop()