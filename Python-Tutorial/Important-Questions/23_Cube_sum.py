r = list(map(int, input().split()))

sum = 0
for i in range(r[0], r[1]+1):
    sum += i**3
print(sum)