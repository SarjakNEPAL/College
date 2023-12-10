# Accept the following from the user and calculate the percentage of class attended:
#a. Total number of working days
#b. Total number of days for absent
#After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.

td=int(input("Enter total number of working days"))
ad=int(input("Enter total number of abscent days"))
p=(ad/td)*100
if 100-p<75:
    print("NOT ELIGIBLE FOR EXAM")
else:
    print("Eligible for exam")