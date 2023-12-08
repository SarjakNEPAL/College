#Date 8 octuber 
a="python"
print(a.capitalize()) # capitalizes 1st
print(a.title()) #capitalizes all the word's initials
print(a.rjust(9,"*"))# total no os string + the space u need to ad. The funcetion adds some space before the sring
print(a.ljust(9,"*"))# ''                      ''            after  the string
print(a.center(12,"*")) #refer copy no 115
#######TASK################
#display **softwarica*** using center function
b="softwarica" #variable initial
c=b.center(16,"*") # added * 
print(c[1:]) # sliced print from 2nd position
print(a.zfill(9)) # used to add 0 before the string 
#########End###################
#for the + and - in string the O is added after these but fOR OTHER it gets BEFORE EG: +1sar  ,  1$sar.
#case changing
print(a.upper()) # transform to all uppercase
print(a.lower())#transforms all to lowercase
print(a.swapcase())# changes upper to lower and lower to upper
#Finding charCTER
print(a.find("y"))# a---->b checking the string first answer and exists
print(a.rfind("y"))#a<----b checking the string first answer ;exit; positive value return
#no of characters
m="apple"
print(m.count("p")) # counts the number of repetations
#checking whether the case / datatype is not
print(m.isupper())#IS all uppercare nr not
print(m.islower())#is all lowercase or not
print(m.isdigit())#is all intiger or not
print(m.isalnum())#is all alphabert and number or not
print(m.isalpha())#is all alphabet or not
#other checking 
print(a.isspace())#whether if all the input is <SPACE>
#\t \n are not affected and if kept inside the the input the input is true
print(a.isidentifier())#whether the givern value complies with identifier rules
print(a.isprintable())#whether the all input can get displayes or not eg:py\thon is false python is true. escape character false
print(a.istitle())#checks whether the string is title(aLL THE initial letter are capital or not) 
##############task###########
print("#"*10)
a="python"
b="Hello world"
c="Pythons"
d="\t"
e="123"
f="123python"
print(a.capitalize())
print(b.title())
print(a.ljust(10,"*"))
print(a.rjust(10,"*"))
print(a.center(10,"*"))
print(c.center(12,"*"))


