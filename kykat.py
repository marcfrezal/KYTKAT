#! /usr/bin/python3

from tkinter import *

window = Tk()

var_str = StringVar()
var_int = IntVar()

cadre = Frame(window, width=700, height=800, border=1)
cadre.pack(fill=BOTH)
text_two = Label(cadre, text="Kalash Krimi")
text_two.pack(side="right", fill=X)




text = Label(window, text="JUL EN Y")
button = Button(window, text="bye", command=quit)
text_box = Entry(window, text=var_str, width=30)
box = Checkbutton(window, text="Coche moi si t'es cap", var=var_int)

box.pack()
text_box.pack()
button.pack()
text.pack()
window.mainloop()