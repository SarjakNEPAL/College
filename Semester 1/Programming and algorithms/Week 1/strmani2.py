# rjust
a="hello world" #11

print(a.rjust(15,"#")) # it will add (length of str - supplied string left at side) 
print(a.ljust(15,"#"))#     ''    ''        ''                ''      right
print(a.center(20 ,"#"))# refer copy 115

print(a.zfill(16))# adds 0 before string (length oof string + number of 0 wanted) should be supplied 


print(a.upper()) #makes all capital
print(a.lower()) #makes all lower
print(a.swapcase())# makes capital small and small capital

# searching for character 
print(a.find("w")) # searches character with a -------> b
print(a.rfind("l"))   # searches character with a <------- b

b="book cook meeeaow"
#counting the characters 
print(b.count("o"))

print(b.isspace()) # checks whether all the character is space or not
print(b.islower())
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
print("finish till week 1")