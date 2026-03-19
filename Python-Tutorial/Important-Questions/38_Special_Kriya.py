# m -> distinct circular series
# n -> length of n in each circular series no. 1 to n

m = int(input())
n = int(input())

l = []
for i in range(n):
    l.append(i+1)

sum = 0
length = len(l)
for i in range((length-1),0,-2):
    sum += l[i]
print(sum * m)
