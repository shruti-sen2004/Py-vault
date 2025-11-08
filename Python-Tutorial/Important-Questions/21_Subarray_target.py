arr = list(map(int,input().split()))
target = int(input())

sumMap = {}
current_sum = 0

for i in range(len(arr)):
    current_sum += arr[i]
    if current_sum == target:
        print(arr[:i+1])
    if current_sum - target in sumMap:
        start= sumMap[current_sum-target] +1
        print(arr[start: i+1])
    sumMap[current_sum] = i

print(sumMap)