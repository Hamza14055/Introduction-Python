from tkinter import *
window= Tk()
window.title="Event Handler"
window.geometry=("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def button_press(event):
    print("\n A button just got clicked!")
button = Button(text="click me")
button.pack()
button.bind("<Button-1>",button_press)
window.mainloop()