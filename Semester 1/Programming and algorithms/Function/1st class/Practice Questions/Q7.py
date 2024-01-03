#reverse a list

def rev(a):
    temp=[]
    for i in range(len(a)-1,-1,-1):temp.append(a[i])
    return temp

g=[1,23,4,52,234,234,33]
print(rev(g))