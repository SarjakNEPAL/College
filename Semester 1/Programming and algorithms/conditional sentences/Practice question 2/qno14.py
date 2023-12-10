#14. Accept the number of days from the user and calculate the charge for library according to following:
#Till five days: Rs 2/day
#Six to ten days: Rs 3/day
#11 to 15 days: Rs 4/day
#After 15 days: Rs 5/day

a= int(input("Enter Number of days"))
if a>=15:
    c=a*5
elif a<15 and a>=11:
    c=a*4
elif a<11 and a>5:
    c=a*3
elif a<5 and a>=0:
    c=a*2
else:
    c=-1
if c!=-1:
    if a==1:
        print((f"Charge for a day is {c} "))
    else:
        print(f"Charge for {a} days is {c} ")
else:
    print(f"Enter Valid input")