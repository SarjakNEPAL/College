#write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
l=[1,"a","c",2,3,4]
for i in range(len(l)):
    if isinstance(l[i],int):
        print(l[i])