from tkinter import *
from PIL import Image, ImageTk # for jpg images

root = Tk()

#HeightXWidth
root.geometry("1200x690")

photo = PhotoImage(file="./Tkinter Course/logo.png")
label = Label(image=photo)
label.pack()

# #For JPG images

# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)

root.mainloop()