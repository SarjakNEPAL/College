from tkinter import *
from sqlite3 import *

root=Tk()
lbl=Label(root, text="Employee Management System",font=("Arial Bold",50))
lbl.place(x=200,y=0)
root.geometry("1500x1500")
root.resizable(False,False)

def clrfld():
        username.delete(0,END)
        address.delete(0,END)
        role.delete(0,END)
        salary.delete(0,END)

def Retrieve():
    conn=connect("genderdb.db")
    c=conn.cursor()
    c.execute("SELECT * FROM employee")
    records= c.fetchall()
    print_records=''
    for record in records:
        print_records +=str(f'{record[0]}   {record[1]}         {record[2]}    {record[3]}     {record[4]} \n')
    query_label=Label(root,text=print_records)
    query_label.place(x=0,y=500)

def add(): 
    conn=connect('genderdb.db')
    c=conn.cursor()
    c.execute("INSERT INTO employee(uname,adr,rl,slr) VALUES(?,?,?,?)",(username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    clrfld()



conn=connect("genderdb.db")
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               uname TEXT,
               adr TEXT,
               rl TEXT,
               slr INT
)''')

conn.commit()
conn.close()



label_username=Label(root,text="Username",font=("Aroal Bold",20))
label_Salary=Label(root,text="Salary",font=("Aroal Bold",20))
label_Address=Label(root,text="Address",font=("Aroal Bold",20))
label_Role=Label(root,text="Role",font=("Aroal Bold",20))
label_Delete=Label(root,text="Delete Record",font=("Aroal Bold",20))



username=Entry(root, width=30)
address=Entry(root, width=30)
role=Entry(root, width=30)
salary=Entry(root, width=30)
delete_box=Entry(root,width=25)




label_username.place(x=10,y=100)
label_Salary.place(x=10,y=150)
label_Address.place(x=10,y=200)
label_Role.place(x=10,y=250)
label_Delete.place(x=10,y=300)



username.place(x=170,y=100,height=30)
address.place(x=170,y=150,height=30)
role.place(x=170,y=200,height=30)
salary.place(x=170,y=250,height=30)
delete_box.place(x=200,y=300,height=30)

btn_add=Button(root,text="Add",font=("Arial Bold",20),command= lambda: add())
btn_Retrieve=Button(root,text="Retrieve",font=("Arial Bold",20),command= lambda: Retrieve())
btn_delete=Button(root,text="delete",font=("Arial Bold",20),command= lambda: add())

btn_add.place(x=50,y=370)
btn_Retrieve.place(x=150,y=370)
btn_delete.place(x=300,y=370)





root.mainloop()
