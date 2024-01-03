#given list is [1,2,3,4] but expected output in new list [2,3,4,5]
def ecad(a,n):
    temp=[]
    for i in a:
        temp.append(i+n)
    return temp
print(ecad([1,2,3,4],1))
