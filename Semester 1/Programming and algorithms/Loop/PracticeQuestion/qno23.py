#Python program to count the space of a given string
a=input("Enter string")
s=0
for i in a:
    if i.isspace():
        s+=1
print("no of space = %d"%(s))
