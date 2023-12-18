# Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a=["ram","shyam"]
b=[]
for i in a:
    b.append(f"Dr.{i}")
print(b)
