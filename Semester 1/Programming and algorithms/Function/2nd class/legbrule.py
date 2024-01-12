from math import pi
# pi=10
a=10
def add():
    a=20
    def inner():
        a=30
        print(pi)
    inner()
add()


#with math fucn