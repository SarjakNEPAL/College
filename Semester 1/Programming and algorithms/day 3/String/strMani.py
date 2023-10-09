#replaceing the DATA of the string
a="Bye Bye world"
#replace
c=a.replace("w","W").replace("B","b")
#make trans
d=a.maketrans("By","Be")
print(c)
#displaying without translate
print(d)
#translate method
print(a.translate(d))
