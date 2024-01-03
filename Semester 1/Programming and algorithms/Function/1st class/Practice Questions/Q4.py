#write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

def dekhaint(t=[1,"a","c",2,3,4]):
    for i in t:
        if isinstance(i,int):print(i,end="\n")
dekhaint()
