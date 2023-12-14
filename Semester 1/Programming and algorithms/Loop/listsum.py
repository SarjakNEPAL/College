a=[1,2,3,4,5]
sum=0
mult=1
for i in range(0,len(a)):
    sum=sum+int(a[i])
    mult=mult*int(a[i])
print("Sum =", sum,sep=" ",end="\n")
print("multiplication= {}".format(mult),end="\n")
