#Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
def sepa(a):
    temp=[]
    for i in a:
        temp.append(type(i))
    return temp


lst=[1,2,3,"d",4,5,"a"]
stri=sepa(lst)
print(F"datatypes={stri}")