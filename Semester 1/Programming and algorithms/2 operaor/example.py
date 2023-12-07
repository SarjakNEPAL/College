# Operators

# This is print statements 
print("hello world")

a=5 #variable a holds value 5
b=10 # assignining value 10 to b
c=a+b  # Adding values 
print("sum =",c) # printing the statement 

def add(a1,a2):
    """
        Adds two numbers a1 and a2 and returns the results
        Arguements:
            a1=decimal integer
            b2=decimal integer
        return:decimal integer
    """
    return a1+a2
print(add(a,b))
print(add.__doc__)

# is and in operators: is operatior is used to compare memory location of the variable. 
# in operator is used to check the character inside the string
print(a is  b)
print(a is not(b))
k= "apple"
print("l" in k)
    
print(bin(2*b)) # gives binary

a = 21

b = 10

if (a == b):
    print(" a is equal to b")
else:
    print("a is not equal to b")
if (a != b):
    print(" a is not equal to b")
else:
    print("a is equal to b")
if (a<b):
    print(" a is less than b")
else:
    print("a is not less than b")
if (a > b):
    print(" a is greater than b")
else:
    print(" a is not greater than b")

# bitwise operation
kk=a&b
print("value of kk is", kk)


# using not operator bitwise
u=10 #assign value (bianry value is 1010)
# the output by the system is 
print(~u)

# performing the one's complement and 2's complement
# first the binary value is stored 
print("-",a+1)

print(f"{0.1:.20}")
print(f"{0.2:.20}")
print(f"{0.3:.20}")


# performing  