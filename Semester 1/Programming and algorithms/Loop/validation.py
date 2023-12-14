# eamil must have @gmail.com 
# password length must be greater and have special characters
# more than 3 times attemmpt invalid

fa=3
succ=False
speci=False
em=False
while fa>0 and succ!=True:
    print(f"No of attempt left={fa}") 
    em=input("enter email")
    if em.endswith(".com") and "@" in em:
        pss=str(input("Enter Password"))
        if len(pss)>8:
            j=pss
            if "@" in j  or "!" in j or "$" in j or "%" in j or "_" in j or "-" in j or "=" in j:
                speci=True
                succ=True
            elif speci!=True:
                print("Enter special character in the password")
                fa-=1
        else:
            print("Password must be more than 8 characters")
            fa-=1
    else:
        print("Enter valid Email")
        fa-=1

if fa==0 and succ!=True: print("Blocked")
elif succ==True: print("Logged in")
