# multiplication table of a given number
a=int(input("Enter the number to find multilication table of"))
for i in range(0,int(input("From 0 to ?"))+1,1):print("{} X {} = {}".format(a,i,a*i))