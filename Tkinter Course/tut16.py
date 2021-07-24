from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def getdollar():
    print(f"We have credited ${myslider2.get()} dollars to your bank")
    tmsg.showinfo("INFO",f"We have credited ${myslider2.get()} dollars to your bank")

root.geometry("700x400")
root.title("Slider Tutorial")\

# myslider = Scale(root,from_=0, to=455)
# myslider.pack()

Label(root, text="How many dollars do you want?").pack()

myslider2 = Scale(root,from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(34)
myslider2.pack()

Button(root, text="Get Dollars!", command=getdollar).pack()

root.mainloop()