from string import Template
a=int(input("enter a number"))
c=""
if a%2==0 and a%3==0:
    c="divisible"
else:
    c="not divisible"
print(Template("$k is $kk with 2 and 3 both").substitute(k=a, kk=c))
