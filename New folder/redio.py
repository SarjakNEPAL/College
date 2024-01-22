#radio is a button which only user can collect 
from tkinter import *

a=Tk()
a.geometry("800x800")
a.config(bg='yellow')

global i
i=0
def clicked():
    if var.get()%2==0:
        a.config(bg="Pink")
        k.config(text="Female")
    else:
        a.config(bg="Blue")
        k.config(text="male")
k=Label(a,text="gender select")
k.pack(anchor=W)

var=IntVar()
r1=Radiobutton(a,text="Male",variable=var,value=1,command=clicked)
r2=Radiobutton(a,text="Female",variable=var,value=2,command=clicked)
r1.pack(anchor=W)
r2.pack(anchor=W)

a.mainloop()

