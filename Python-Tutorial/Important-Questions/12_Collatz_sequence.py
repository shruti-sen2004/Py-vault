k = int(input())

if k <0 :
    print('Error!!')

max_val = []
max_len = []
for i in range(1, k+1):
    j = i
    arr =[j]
    while j !=1:
        if j %2 ==0:
            j //=2
        else:
            j = j*3+1
        arr.append(j)
    max_val.append([max(arr),i])
    max_len.append([len(arr),i])

print(arr)
print(*max(max_len, key=lambda x: x[0])) # to only compare the value not index
print(*max(max_val, key=lambda x: x[0])) # * -> unpacking operator; prints elements space seperated 


    