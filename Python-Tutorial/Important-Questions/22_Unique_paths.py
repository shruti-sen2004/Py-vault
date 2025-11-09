# M-1 using mathematics combination
import math

index = list(map(int,input().split()))

total_steps = index[0] + index[1] -2 
right= index[1] -1
paths = math.comb(total_steps,right)
print(paths)

# M-2 Dynamic programming

m = int(input())
n = int(input())
row = [1] * n

for i in range(m-1):
    newRow = [1]*n
    for j in range(n-2, -1,-1):
        newRow[j] = newRow[j+1] + row[j]
    row = newRow
print(row[0])