#checkbutton
from tkinter import *

def click():
    if a.get()!="" or b.get()!="" or c.get()!="":
        k.config(text=f"You like : {a.get()}{b.get()}{c.get()}")

app=Tk()
a=StringVar()
b=StringVar()
c=StringVar()

k=Label(app,text="You like:")
c1=Checkbutton(app,text="Music",variable=a,onvalue="Music", offvalue=".",height=5,width=20)
c2=Checkbutton(app,text="Food",variable=b,onvalue=", Food", offvalue=".",height=5,width=20)
c3=Checkbutton(app,text="Cat",variable=c,onvalue=", Cat", offvalue=".",height=5,width=20)
k.pack()
c1.pack()
c2.pack()
c3.pack()
btn=Button(app,text="Click",command=click)
btn.pack()

app.mainloop()