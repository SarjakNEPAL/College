#Given list is [1,2,3,4] but expected output is [1,"a",2,4]

def nl(a):
    temp=[]
    for i in range(0,len(a)):
        r=a[1]
        if i==1:temp.append("a")
        elif i==2:temp.append(r)
        else: temp.append(a[i])
    return temp

print(nl([1,2,3,4]))