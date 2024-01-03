# Given list is lst=[1,2,3,4] but print 1 and 4 only 
def c(a):
    for i in range(0,len(a),3):print(a[i])
c([1,2,3,4])