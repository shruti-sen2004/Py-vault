# M-1 sliding windpw       O(N.K)
arr = list(map(int, input().split()))
k = int(input())

# for i in range(len(arr)):
#     sub_array = arr[i:i+k]
#     if len(sub_array) == k:
#         print(max(sub_array),end=" ")

# M-2 monotonic deque        O(N)
from collections import deque

def max_subarray(arr,k):
    dq = deque() # stores indices not values, d[0] index with max val
    result =[]

    for i in range(len(arr)):
        while dq and arr[dq[-1]] <= arr[i]: # monotonic - element smaller than new one removed
            dq.pop()
        dq.append(i) # add current index back
        if dq[0] == i-k: # front element too old
            dq.popleft()
        if i>= k-1: # window fully formed
            result.append(arr[dq[0]])
    return result
print(*max_subarray(arr,k))