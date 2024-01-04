#Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

def sepa(a,dat):
    temp=[]
    for i in a:
        if(isinstance(i,dat)):temp.append(i)
    return temp


lst=[1,2,3,"d",4,5,"a"]
stri=sepa(lst,str)
inti=sepa(lst,int)
print(F"Integer = {inti}\nStrings={stri}")
