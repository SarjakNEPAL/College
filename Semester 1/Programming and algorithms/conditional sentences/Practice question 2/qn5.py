#Check whether the user input number is even or odd and display it to user.

a= int(input("enter a number"))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")