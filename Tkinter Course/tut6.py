from tkinter import *

root = Tk()

root.geometry("1200x690")
root.title("Labels")

#Important Label Options
# text = adds the textbd = background
# fg = foreground
# font = set the font
# padx = x padding
# pady = y padding
# relief = border styling  (SUNKEN, RAISED, GROOVE, RIDGE)

title_label = Label(text='''Shah Rukh Khan (pronounced [ˈʃaːɦrʊx xaːn]; born 2 November 1965), also known by the initialism SRK, is an Indian actor, film producer,
\nand television personality. Referred to in the media as the "Baadshah of Bollywood" (in reference to his 1999 film Baadshah), 
\n"King of Bollywood" and "King Khan", he has appeared in more than 80 Hindi films, and earned numerous accolades, including 14 Filmfare Awards.
\nThe Government of India has awarded him the Padma Shri, and the Government of France has awarded him the Ordre des Arts et des Lettres and the Legion of Honour.
\nKhan has a significant following in Asia and the Indian diaspora worldwide. In terms of audience size and income, he has been described
\nas one of the most successful film stars in the world.''' , 
bg="red", fg="white", padx =23, pady=94, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)

#Important Pack options

# anchor = nw,ne
# side = top,bottom,left,right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor="se",fill=X)
title_label.pack(side=RIGHT, anchor="se",fill=Y, padx=34, pady=34)

root.mainloop()