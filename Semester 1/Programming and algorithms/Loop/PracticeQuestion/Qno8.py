#given list is [1,2,3,4] but expected output in new list [2,3,4,5]


lst=[1,2,3,4]
temp=[]
for i in range(0,len(lst)):
    temp.append(lst[i]+1)
lst=temp
print(lst)
