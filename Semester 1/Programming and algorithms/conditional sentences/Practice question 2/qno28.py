#Write a program to check whether a number entered is three digit number or not.
a=int(input("Enter digits"))
if(len(str(a)) ==3):
    print(f"{a} is 3 digit number")
else:
    print(f"{a} is not 3 digit number")
