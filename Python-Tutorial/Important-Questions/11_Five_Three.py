arr = input()[1:-1].split(" ")
s = ""

for i in arr:
    if int(i) % 3 ==0 and int(i) % 5 ==0:
        i ="ThreeFive"
    elif int(i) % 3 ==0:
        i = "Three"
    elif int(i) % 5 ==0:
        i = "Five"
    else:
        pass
    s += i + ' '
print(s)

## to replce space in between use .replace(" ", "")