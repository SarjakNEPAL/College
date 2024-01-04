#Given list is lst=[1,2,3,4] but print 1 2 and 4 only 

def tsk(a):
    for i in range(4):
        if a[i]!=3:print(a[i])
        else:continue
tsk([1,2,3,4])