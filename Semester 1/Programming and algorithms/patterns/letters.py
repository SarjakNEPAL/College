# first define column and row
for row in range(6):
    for column in range(5):
        if column==0 and row!=0:print("*",end=" ")
        elif (column!=0 and column!=4) and (row==0 or row ==3):print("*",end=" ")
        elif column==4 and row!=0:print("*",end=" ")
        else:print(end="  ")
    print()