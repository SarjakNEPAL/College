#given list is [1,2,3,4] but expected output is [1,8,27,64]
a=[1,2,3,4]
b=[]
for i in a:b.append(i**3)
print(f"{b}")