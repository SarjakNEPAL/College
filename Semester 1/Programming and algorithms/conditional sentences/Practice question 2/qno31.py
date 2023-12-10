# . Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
#Age                  Sex    Wage/day
#>=18 and <30          M       700
#                      F       750
#>=30 and <=40         M       800
#                      F       850

s=input("Male or Female ")
g=int(input("enter age "))
a=s.lstrip().upper().rstrip()
d=int(input("enter number of days" ))
w=0
if (a=="M" and len(a)==1) or a=="MALE"  :
    if g>=18 and g<30:
        w=700
    elif g>=30 and g<=40:
        w=800
    else:
        w=-1
    
elif (a=="F" and len(a)==1) or a=="FEMALE"  :
    if g>=18 and g<30:
        w=750
    elif g>=30 and g<=40:
        w=850
    else:
        w=-1
else:
    print("No such sex")

if w!=-1:
    tw=d*w
    print("Wage is {}".format(tw))
else:
    print("Child Labour")