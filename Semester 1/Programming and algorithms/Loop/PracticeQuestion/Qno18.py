#factorial of a given number
a=int(input("Enter the number"))
fac=1
for i in range(a,0,-1):
    fac=fac*i
print(f"{a}!={fac}")
