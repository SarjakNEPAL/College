#A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
#The program should read three integers: the number of students in each of the three 
#classes, a, b and c respectively.
#Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. 
#The second group has 21 students, so they can get by with no fewer than 11 desks. 
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
import math
s=int(input("Enter no of students in 1st class"))
s1=int(input("Enter no of students in 2ND class"))
s2=int(input("Enter no of students in 3RD class"))

if s>0:
    dsk1=math.ceil(s/2)
    dsk2=math.ceil(s1/2)
    dsk3=math.ceil(s2/2)
    dsk=dsk1+dsk2+dsk3
else:
    dsk=0
print("no of desk =",math.ceil(dsk),sep=" ") #math.ceil convers to round up
