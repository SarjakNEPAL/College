#  Given list is [1,2,3,4,5] separate the elements into odd and even categories.
a=[1,2,3,4,5]
even=[]
odd=[]
for i in range(0,len(a)):
    if (a[i])%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])

print(f"Odd = {odd}\n")
print(f"Even= {even}\n")
