#multiplication table of a given number

def mut(a,n):
    for i in range (n):print(f"{a} X {i} = {a*i}")
mut(int(input("Enter number")),int(input("Enter Range")))