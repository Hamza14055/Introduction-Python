from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry=("200x200")
window.title=("Message Box")
def msg():
    messagebox.showwarning("alert!!","Stop, virus found!!")
button = Button(window,text="Scan for virus",command=msg)
button.place(x=80,y=40)
window.mainloop()
