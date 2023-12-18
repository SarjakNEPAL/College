#  Python program that accepts a string and calculate the number of digits and letters and space

a="Betty Bought 1 butter and 8 apples"
s=0
d=0
l=0

for i in a:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
print(f" No of spaces ={s} \n No of digits={d} \n number of letters={l} ")
