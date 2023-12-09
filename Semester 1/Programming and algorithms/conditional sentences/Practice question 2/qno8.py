# Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
#Cost price(in Rs)                  Tax
#>100000                              15%
#>50000 and <=100000      10%
#<=50000                               5%

a=int(input("enter cost of bike"))
if a>100000:
    tax=(15/100)*a
elif a<=100000 and a>50000:
    tax=(10/100)*a
else:
    tax=(5/100)*a
print(f"Tax for {a} is {tax}")
