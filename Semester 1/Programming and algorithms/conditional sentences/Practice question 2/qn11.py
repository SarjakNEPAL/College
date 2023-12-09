#11. Accept the percentage from the user and display the grade according to the following criteria:
#Below 25 --D
#25 to 45  -- C
#45 to 50 -- B
#50 to 60 --B+
#60 to 80 -- A
#Above 80 -- A+

a=int("enter percentage")
if(a>80):
    print("A+")
elif(a<=80 and a>60):
    print("A")
elif(a<=60 and a>50):
    print("B+")
elif(a<=50 and a>45):
    print("B")
elif(a<=45 and a>25):
    print("C")
else:
    print("D")
