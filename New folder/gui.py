from tkinter import *
from tkinter import messagebox
# global ak
# ak=0
# app=Tk()
# app.geometry("300x300")
# e1=Entry(app)
# e1.pack()
# a=Label(app,text="hello")
# def clk():
#     global ak
#     if ak%2==0:
#         a.config(text="Hello")

#     else:
#         a.config(text="World")
#     ak=ak+1
# b=Button(app,text="Clickme",command=clk)
# a.pack()
# b.pack()
# app.mainloop()
# # print(e1)

# app=Tk()
# app.geometry("500x500")
# kk=Entry(app)
# c=Label(app,text="")
# c.pack()
# kk.pack()
# Button(app,text="Okay",command=lambda:c.config(text=f"{kk.get()}")).pack()
# Button(app,text="reset",command=lambda: kk.delete(0,END)).pack()

# app.mainloop()

app=Tk()
app.geometry("1000x1000")
app.config(bg="yellow")
n=Label(app,text="Name:")
n1=Label(app,text="Last:")
n2=Label(app,text="Gender:")
n3=Label(app,text="Age:")
n4=Label(app,text="")
e1=Entry(app)
e2=Entry(app)
e3=Entry(app)
e4=Entry(app)
b1=Button(app,text="Ok",command=lambda: messagebox.showinfo("Success",f"Hello {e1.get()} {e2.get()}.\n You are {e4.get()} years old. \n Your gender is {e3.get()}\n you wrote \" {txt.get(1.0,END)}\"") )
txt=Text(app,width="30",height="5")
n.place(relx=0.1,rely=0.1)
e1.place(relx=0.4,rely=0.1)
n1.place(relx=0.1,rely=(0.2))
e2.place(relx=0.4,rely=(0.2))
n2.place(relx=0.1,rely=(0.3))
e3.place(relx=0.4,rely=(0.3))
n3.place(relx=0.1,rely=(0.4))
txt.place(relx=0.1,rely=0.5)     #float value will be index eg frst will be 1.0
e4.place(relx=0.4,rely=(0.4))
b1.place(relx=0.5,rely=0.7)
n4.place(relx=0.1,rely=0.9)

app.mainloop()