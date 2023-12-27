ls=[1,2,3,4,5,6,7,8,9]
i=0
s=1
while i<len(ls):
    s*=ls[i]
    i=i+1
print("Multiplication  of each element of {} ={}".format(ls,s))