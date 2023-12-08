a=int(input("enter number"))
months={1:"January",2:"february",3:"March", 4:"April",5:"May",6:"June",7:"July"}
if a>0 and a<7:
    print("Month is {mm}".format(mm=months[a]))
else:
    print("enter a valid Number (1 to 7)")