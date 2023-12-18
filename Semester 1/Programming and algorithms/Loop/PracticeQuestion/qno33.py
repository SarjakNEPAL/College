#Write a for loop which appends the type of each element in the first list to the second list.
a=[1,"a",1.1]
b=[]
for i in a:b.append(type(i))
print(b)
 