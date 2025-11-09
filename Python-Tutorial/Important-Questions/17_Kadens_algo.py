arr = list(map(int, input().split()))

max_sum = arr[0]
curr_sum = 0

for i in range(len(arr)):
    curr_sum += arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum =0
print(max_sum)