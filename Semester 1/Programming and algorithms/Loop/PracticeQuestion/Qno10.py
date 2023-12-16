#Given list is lst=[1,2,3,4] but print 1 2 and 4 only 
t=[1,2,3,4]
for i in range(0,len(t)):
    if(t[i]!=3):
        print(t[i])