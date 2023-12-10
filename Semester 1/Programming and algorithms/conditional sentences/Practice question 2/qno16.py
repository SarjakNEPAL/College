#Write a program to check two strings are anagram or not.
a=str(input("Enter a word"))
b=str(input("Enter a word"))
d=a.upper()
e=b.upper()
f=len(a)
g=len(b)
ana=False
if f==g:
    if sorted(d)==sorted(e):   # sorted function sorts according to acending order and converts to list
        ana=True
if(ana==True):
    print("Its an anagram")
else:
    print("Its not an anagram")