n = int(input())

flag =0
prev2, prev = 0, 1
if n == 0:
    print(prev2)
    flag = 1  
if n == 1:
    flag = 1  

fibSum = 1
for i in range(2, n):
    cur = prev2 + prev 
    fibSum += cur
    prev2, prev = prev, cur

if flag ==0:
    print(fibSum)