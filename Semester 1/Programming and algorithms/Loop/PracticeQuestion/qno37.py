# Python program to count the number of even and odd numbers from a series of numbers.  
o=0
e=0
for i in range(100):
    if i%2==0:e+=1
    else: o+=1
print(F"Even = {e} \nodd = {o}")