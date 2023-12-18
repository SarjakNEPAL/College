#removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"]

s = "py;th* o:n ! ;py * t*h:o !n"
bd=False
d=""
for i in s:
    for a in bad_chars:
        if i==a:
            bd=True
        else:
            continue
    if bd==False and not(i.isspace()):print(i,end="")
    bd=False

        