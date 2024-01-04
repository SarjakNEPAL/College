# Given list is [1,2,3,4,5] separate the elements into odd and even categories.

def futal(a):
    o=[]
    e=[]
    for i in a:
        if i%2==0:e.append(i)
        else: o.append(i)
    print(f"Odd elements = {o} \nEven elements ={e}")
futal([1,2,3,4,5])