from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def order():
    tmsg.showinfo("Order Recieved",f"We have recieved your order for {var.get()}")

root.geometry("700x400")
root.title("Radio Button")

# var = IntVar()
var = StringVar()
var.set("Samosa")

Label(root, text="What would you like to have?",font="lucida 19 bold", justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="Dosa",padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idli",padx=14, variable=var, value="Idli").pack(anchor="w")
radio = Radiobutton(root, text="Paratha",padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa",padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order", command=order).pack()

root.mainloop()