#tuple value addition using type casting

a=(1,2,3,4,5)
b=list(a)
b.insert(2,"ram")
print(tuple(b))




a={"a":1}
print(a.setdefault("a","momo"))
print(a.setdefault("c","momo"))
print(a)

a["a"]:6
print(a)


oldkey='a'
newkey='z'
a[newkey]=a.pop(oldkey)
print(a)

for i in a.keys():
    print(i)
