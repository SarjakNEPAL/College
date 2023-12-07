from string import Template
a=1
print(a.real)  
print(a.imag)

# in real part everthing isa alowed but in img omly integers and float are allowed
# a=1, is tuple

b=2,3
print(type(b))

#in set we cannot put multiple similar datas it is not possible to perform indexing and slicing but we can remove and add datas
# using pop and append functions. 

# dictionary stores in key value, dictionary: indexing is not allowed we must use key, 

print(isinstance(a,int)) # checks whetherthe datatype is same or not
print("s",a,b,sep=",",end="\n")
print(2020,10,2,sep="/")
print("hello python", sep="/") # sep does not work on single string object

print("yudip",end="") # line brak is ignored
print("yudip ")

# string formating, redesigining a predefined text/ adding value or variabke in a text . 
# old method c-style, templete, insert
# c style 
print("my name is %s and my age is %d"%("ram", 33)) # same like in C programming but a bit different in syntax. 
# format method
print("yudip is {} and he is very {}".format("handsome","strong")) # default arguement
print("yudip is {1} and he is very {0}".format("handsome","strong")) # positional arguement
print("yudip is {koko} and he is very {lolo}".format(koko="handsome",lolo="strong")) # keyword arguement
# u cannnot use indexing for example .format(koko,lolo) is not allowed, value must be supplied inside the formatting 
print("yudip is {0} and he is very {name}".format("handsome",name="strong"))
# we must use positional arguemnet before the keyword while assigining the values 
print(f"yudip is {a} and he is very {b}")

c="kokoloko"
m="toko"
print(Template('$c $m').substitute(c=c,m=m)) 
ll=-92
print(bin(-92))
# 1 1011100 1= negetive 
# 0 0100011
# 0 0100100
# 0 1011011
print(int("1011011",2))

kk="Apple   "
print(kk.rstrip())