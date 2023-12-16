#armstrong or not
p=input("Enter number")
c=len(p)
re=0
for i in p:
    re+=int(i)**c
if int(re)==int(p):
    print("It is armstrong number")
else: 
    print("Not an armstrong number")