#sum in a list
a=[]
sum=0
n=int(input("Enter number of items in the list"))
for i in range(n):
    a.append(input(f"Enter Data for item no {i+1} in list"))
for i in range(len(a)):
        sum=sum+int(a[i])
        print(a[i],end="")
print(f"sum= {sum}")