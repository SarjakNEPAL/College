#DAY 3

a= 1
b= 1
c=4
d="abc"
e="abc"
f="cde"


#Here are some functions
#1. ID: this shows the object referece of the pointer. Here if a = 1 then 1 points to a and a points to it's object reference
#2. Type(): this shows the datatype of the data stored in the variable
#3: is: it is used to compare object references two datas or variable and if correct gives true else false if

# using these with the variables with same datas 
print("a=",a,"b=",b,sep=" ",end='\n')
print("datatype of a and b =",type(a),"and", type(b),end="\n")
print("object identifier of a=",id(a),"\n object reference of b=",id(a),sep=" ",end=".\n")
print(id(a) == id(b))# this checks wheter the object identifier of both variables are same or not. here it has same values in integer so it gives true  


# using these with the variables with same datas 
print("d=",d,"e=",e,sep=" ",end='\n')
print("datatype of d and e =",type(d),"and", type(e),end="\n")
print("object identifier of d=",id(d),"\n object reference of e=",id(e),sep=" ",end=".\n")
print(d is e)# this checks wheter the object identifier of both variables are same or not. here it has same values in integer so it gives true  

# using these with the variables with not same datas 
print("d=",d,"f=",f,sep=" ",end='\n')
print("datatype of d and e =",type(d),"and", type(e),end="\n")
print("object identifier of d=",id(d),"\n object reference of f=",id(f),sep=" ",end=".\n")
print(d is f)# this checks wheter the object identifier of both variables are same or not. here it has same values in integer so it gives true  


#4) .real .img
g=3+2j #here it is imaginary number
print(g.real, g.imag)
