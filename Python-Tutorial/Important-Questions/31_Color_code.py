# arrange in order of highest priority (0) to lowest priority(2)

s = list(map(int,input().split(',')))

# M-1 using sort func
# s.sort()

# for i in range(len(s)):
#     if i != len(s)-1:
#         print(s[i],end=",")
#     else:
#         print(s[i]) 

# M-2 without sort func
i,j = 0,0
k = len(s)-1

# Dutch National Flag Algo
while(j <= k):
    if s[j] == 1:
        j = j+1
    elif s[j] == 2:
        s[j],s[k]= s[k],s[j]
        k = k-1
    else:
        s[j], s[i] = s[i],s[j]
        i = i+1
        j = j+1
print(s)