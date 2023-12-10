#Write a program to accept percentage and display the category according to the following criteria:
#Percentage                                   Category
#<40                                      Failed
#>=40 and <55                             Fair
#>=55 and <65                             Good
#>=65                                     Excellent    

a=int("enter percentage")
if(a>=65):
    print("Excellent")
elif(a<65 and a>=55):
    print("Good")
elif(a>=40 and a<55):
    print("Fair")
else:
    print("D")
