from tkinter import *
root =Tk()
root.title ="Number Pad"
root.geometry =('250x300')
nums = [[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    root.rowconfigure(i,weight=1)
    for j in range(0,3):
         root.columnconfigure(j,weight=1)
         frame = Frame(master=root,relief=SUNKEN,borderwidth=1)
         frame.grid(row=i,column=j,stick="nsew",padx=5,pady=5)
         label = Label(master = frame,text = nums[i][j],bg='#d0efff')
         label.pack(padx=10,pady=10)
root.mainloop()