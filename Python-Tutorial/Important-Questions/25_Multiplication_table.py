n = int(input())

sum =0
for i in range(1,n+1):
    print(f'{n} x {i} = {n*i}')
    sum += (n*i)
print(sum)