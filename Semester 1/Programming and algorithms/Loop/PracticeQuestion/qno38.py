#Write a python program to display all the prime numbers within a given range.
a=int(input("enter Range"))

for i in range(1,a):
    f=0
    for a in range(i,0,-1):
       if i%a==0:
            f+=1
    
    if f==2: print(i)
            

        