e=input("Enter Email")
if("@" in e):
    p=input("Enter Password")
    if len(p)>=8:
        if "@" in p or "!" in p or "$" in p or "%" in p or "_" in p or "-" in p or "=" in p:
            print("Logged in")
        else:
            print("No special characters found")
    else:
        print("Password must contain at least 8 characters")
else:
    print("Enter Valid Email")