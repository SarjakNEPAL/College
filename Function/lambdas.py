from functools import *
#mappings 

marks=[10,20,30]
a=list(map(lambda x:x+2,marks))
print(a)

#filter

marks=[10,20,30,11,22,33]
a=list(filter(lambda x:x%2==0,marks))
print(a)

#reduce

text=["Hello","I","Good"]
a=reduce(lambda x,y:x+y,text)
print(a)


