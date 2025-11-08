n = int(input())

arr = list(map(int,input().split()))

res = []
left = 0
for num in arr:
    right = len(res)
    res.append(num)
    for i in range(left, right):
        value = res[i] | num
        if (res[-1] != value):
            res.append(value)
    left = right
print(res)
print(len(set(res)))