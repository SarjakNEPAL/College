usr=input("Enter a character")
con=0
if usr.isalpha()==True:
    a=usr.upper()
    if a=="A":
        con=1
    elif a=="E":
        con=1
    elif a=="I":
        con=1
    elif a=="O":
        con=1
    elif a=="U":
        con=1
    if con==1:
        print("{0} is vowel".format(a))
    else:
        print("%s is Consonent"%(a))
else:
    print("Insert Alphabets only")
