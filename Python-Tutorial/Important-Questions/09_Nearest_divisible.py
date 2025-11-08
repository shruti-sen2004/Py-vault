num = sorted(list(map(int,input().split())))

x = round(num[1]/num[0]) # gets the exact amount of times Y is larger than X
num[0] = x * num[0]
print( num[0])
