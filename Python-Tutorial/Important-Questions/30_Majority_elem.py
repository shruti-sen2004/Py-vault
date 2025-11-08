from collections import Counter
n = int(input())

arr = input().split()

freq = Counter(arr)

for key,value in freq.items():
    if value >= n//2:
        print(key)