a=10
b=10
c=10

def addi():
    global a,b   # using thiis bahira ko value lai access garna milcha 
    a=a+10
    b=b+20
    print("2",a,b)
print("1",a,b)
addi()
print("3",a,b) # the changes after addi is saved