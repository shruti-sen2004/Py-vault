arr = list(map(int,input().split()))
target = int(input())

count = 0
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if sum == target:
            count += 1
print(count)