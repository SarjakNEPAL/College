a=[1,2,3,4,5,"a","b","c","d"]
i=0
e=[]
s=[]
d=[]
while i<len(a):
    if isinstance(a[i],str)==True:s.append(a[i])
    elif isinstance(a[i],int)==True:e.append(a[i])
    d.append(type(a[i]))
    i=i+1
print(f"Strings = {s} \nintegers={e} \nDatatype={d}")