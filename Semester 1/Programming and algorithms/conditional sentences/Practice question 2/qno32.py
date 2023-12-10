#Accept three numbers from the user and display the second largest number
a=int(input("1st number"))
b=int(input("2nd number"))
c=int(input("3rd number"))
if (a<b and a>c)or(a>b and a<c):
    print('{} is second largest'.format(a))
elif (b<a and b>c)or(b>a and b<c):
    print('{} is second largest'.format(b))
elif (c<a and c>b)or(c>a and c<b):
    print('{} is second largest'.format(c))
else:
    print("equals")
