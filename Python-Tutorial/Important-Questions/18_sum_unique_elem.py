from collections import Counter
arr = list(map(int,input().split()))
freq = Counter(arr)

sum = 0
for key,value in freq.items(): # short-hand for loop
    if value == 1:
        sum += key
print(sum)