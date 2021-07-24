from tkinter import *

root = Tk()
root.geometry("600x400")

def getvals():
    print("It Works!")


Label(root, text="Welcome to Travels", font="comicsansms 13 bold", pady=15).grid(row=0,column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
payment_mode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emergencyval = StringVar()
paymentmodeval = StringVar()
foodserviceval = IntVar()

nameentry = Entry(root,textvariable=nameval)
phoneentry = Entry(root,textvariable=phoneval)
genderentry = Entry(root,textvariable=genderval)
emergencyentry = Entry(root,textvariable=emergencyval)
paymententry = Entry(root,textvariable=paymentmodeval)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

#checkBox
foodservice = Checkbutton(text="Want to Pre Book your Meals?", variable=foodserviceval)
foodservice.grid(row=6,column=3,pady=5)

# Assign command
Button(text="Submit",command=getvals()).grid(row=7,column=3)

root.mainloop()