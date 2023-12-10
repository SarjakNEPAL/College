#12. A company decided to give bonus to employee according to following criteria:
#Time period of service     Bonus
#More than 10 years            10%
#>=6 and <=10                       8%
#Less than 6 years                 5%

a=int("Enter the time Period")
if a>10:
    bo=10
elif a<=10 and a>6:
    bo=8
else:
    bo=5
print(f"bonus ={bo}")