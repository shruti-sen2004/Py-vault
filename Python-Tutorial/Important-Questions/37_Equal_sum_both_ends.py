# print index for which sum of lhs = sum of rhs

l= list(map(int, input().split()))

sum = 0
for i in l:
    sum += i

ls = 0
for i in range(len(l)):
    rs = sum - ls - l[i]
    if rs == ls:
        print(i)
        break
    else:
        ls += l[i]

