#python program to check a number is perfect number
a=int(input("Enter a number"))
s=0
if True:
    if isinstance(a,int) and a>0:
        for i in range(1,a):
            if a%i==0:s+=i
        if s==a:
            print("Perfect Number")
        else:
            print("Not perfect number")
else: 
    print("Numbers only accepted")

# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.