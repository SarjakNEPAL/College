# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

a=[1,2,3,4,"a","b"]
d=[]
for i in a:
    d.append(type(i))
print(d)