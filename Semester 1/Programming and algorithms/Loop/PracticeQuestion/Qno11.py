# Given list is [1,2,3,4] but expected output is [1,"a",2,4]
a=[1,2,3,4]
d=[]
for i in range(len(a)):
    if i==1:
        temp=a[i]
        a[i+1]=temp
        a[i]="a"
    d.append(a[i])
a=d
print(d)


