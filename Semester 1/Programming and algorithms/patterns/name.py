for r in range(6):
    for c in range(34):
        if (c==0) and (r!=4):print("#",end=" ")
        elif (c==1 or c==2 or c==3 or c==15) and (r==0 or r==3 or r==5):print("#",end=" ")
        elif (c==4) and (r!=1 and r!=2):print("#",end=" ")
        elif (c==6 or c==10 or c==24 or c==28) and (r!=0):print("#",end=" ")
        elif (c==7 or c==8 or c==9 or c==13 or c==25 or c==26 or c==27) and (r==0 or r==3):print("#",end=" ")
        elif (c==12 or c==20 or c==30):print("#",end=" ")
        elif (c==14) and (r==0 or r==3 or r==4):print("#",end=" ")
        elif (c==16) and (r!=4):print("#",end=" ")
        elif (c==18 or c==19 or c==33) and (r==0 or r==5):print("#",end=" ")
        elif (c==21 or c==22) and (r==0):print("#",end=" ")
        elif (c==31) and (r==2 or r==3):print("#",end=" ")
        elif (c==32) and (r==1 or r==4):print("#",end=" ")
        else:print(end="  ")
    print()    