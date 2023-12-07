#day 4
a="a quick brown fox jumped over the crazy lazy dog"
print(a[8:-4]) # start : end string is taken
print(a[0:-3:2]) #start : end : separation 

#escape and tags 
print('hello \n world') # this \n changes thr line to next line
print('hello \r world')# it will start to display after /r
print('hello \t world')# it will display with tabs
print('hello \a world')# it will discard a

#replacing 
c=a.replace('a',"A").replace("o","0") # this just basically replaces the all selected characters with the supplied characters
print(c)

#make trans
d=a.maketrans('quick',"slowr")
print(d) # this will display ascii
print(a.translate(d)) # this will display strings after translating


# capitalization
print(a.title()) # this will capitalize each word's initials
print(a.capitalize()) # this will capitalize 1st word 1st initial
