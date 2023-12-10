#A company decided to give bonus of 5% to employee if his/her year of service is more than 5years.
#Ask user for their salary and year of service and print the net bonus amount.

sal=float(input("Enter your salary"))
ser=int(input("Enter your year of service"))
if(ser>5):
    bon=(5/100)*sal
else:
    bon=0
print(f"Your bonus is{bon}")
