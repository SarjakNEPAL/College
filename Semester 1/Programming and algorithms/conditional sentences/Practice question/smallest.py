a=int(input("1st number"))
b=int(input("2nd number"))
c=int(input("3rd number"))
if a<b and a<c:
    print('{} is smallest'.format(a))
elif b<a and b<c:
    print('{} is smallest'.format(b))
elif c<a and c<b:
    print('{} is smallest'.format(c))
else:
    print("equals")
