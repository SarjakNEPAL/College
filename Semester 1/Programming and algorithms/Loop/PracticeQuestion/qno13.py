# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
a = [1,2,3,"d",4,5,"a"]
s_data=[]
i_data=[]
for i in range(0,len(a)):
    if isinstance(a[i],"str"):
        s_data.append(a[i])
    elif isinstance(a[i],"int"):
        i_data.append(a[i])
print(f"Integers = {i_data}")