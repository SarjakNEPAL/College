#given number is prime or not
i=int(input("enter number"))
f=0
for a in range(i,0,-1):
    if i%a==0:f+=1
if f==2: print("Prime") 
else: print("Not prime")

            
