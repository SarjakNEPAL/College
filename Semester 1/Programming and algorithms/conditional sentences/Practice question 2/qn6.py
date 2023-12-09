# WAP which accepts marks of four subjects and display total marks, percentage and 
#grade.
#Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, 
#less than 40% –> fail

a=int(input("Enter marks of Software Design"))
b=int(input("Enter Marks of programming"))
c=int(input("Enter Marks of maths"))

total= (a+b+c)/3
if total>70:
    print("distinction")
elif total>60 and total<=70:
    print("First")
elif total>40 and total<=60:
    print("Second")
else:
    print("fail")