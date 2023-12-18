#Python program to calculate the sum of all the odd numbers within the given range.
s=0
for i in range(int(input("Enter starting point")),int(input("Enter ending point"))+1,1):
    if i%2!=0:
        s=s+i 
print(F"Sum of odd numbers is: {s}")