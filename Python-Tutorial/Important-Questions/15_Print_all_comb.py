arr= list(map(int,input().split(' ')))

for i in range(1,arr[0]+1):
    j = i
    while j < arr[0]+1:
        print(*arr[i:j+1],end =", ") 
        j += 1       