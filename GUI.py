from tkinter import Button as dabaune
from tkinter import Tk as app
from tkinter import *
from PIL import Image,ImageTk

global k
k=0
def bhan():
    global k
    global image_path
    txt=""
    k=k+1
    if k%3==0:
        txt="Anisha"
        
        root.config(bg="Red")
        a.config(fg="black")
        image_path="D:\\Softwarica\\0.png"
    elif k%3==1:
        txt="Anjali"
        root.config(bg="Blue")
        a.config(fg="Red")
        image_path="D:\\Softwarica\\1.png"
    else:
        txt="kimti"
        root.config(bg="Blue")
        a.config(fg="Red")
        image_path="D:\\Softwarica\\1.png"
    Ad_img = Image.open(image_path)
    a.config(text=f"{txt}")
    ad_pic = ImageTk.PhotoImage(Ad_img.resize((100, 100)))
    # Display the image on a label
    adlabel =Label(root, image=ad_pic, background='#79c2d0')
    adlabel.place(x=30,y=250,width=300,height=300)

root=app()
root.config(bg="Pink")
root.geometry("500x500")
root.title("food")
a=Label(root,text="a",font=("Little Sans",50),fg="Red")
c=dabaune(root,text="thich",command=lambda: bhan())
image_path = '0.png'  # Provide the correct path to your image
Ad_img = Image.open(image_path)

# # Create a PhotoImage object
ad_pic = ImageTk.PhotoImage(Ad_img.resize((100, 100)))

# # Display the image on a label
adlabel =Label(root, image=ad_pic, background='#79c2d0')
adlabel.place(x=30,y=250,width=300,height=300)

c.place(anchor="center",relx="0.1",rely="0.1")
root.iconbitmap("name.ico")
a.place(anchor="center",relx="0.3",rely="0.2")
root.mainloop()





# TKINTER USED