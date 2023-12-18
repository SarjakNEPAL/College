# program to check given number is palindrome or not
a=input("enter multi digit number")
b=""
for i in range(len(a)-1,-1,-1):
   b=b+a[i]
if a==b:
   print("Palindrome")
else:
   print("not palindrome")
