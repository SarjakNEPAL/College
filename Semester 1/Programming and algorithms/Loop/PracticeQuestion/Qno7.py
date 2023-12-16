#reverse a list
a=[]
sum=0
n=int(input("Enter number of items in the list"))
for i in range(n):
    a.append(input(f"Enter Data for item no {i+1} in list"))
print(f"List before reverse is : {a}")
temp=[]
for i in range(n-1,-1,-1):
    temp.append(a[i])
a=temp
print(f"After reverse = {a}")
#another method
a=[1,2,3,4]
b=[]
for i in a:
    b=[i]+b
print(b)