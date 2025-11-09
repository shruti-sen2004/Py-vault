n = int(input())

arr =[]
for i in range(n):
    arr.append(input().split())

def max_cummulative_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i][1]) * int(arr[i][2])
    print(f'\nItem : {arr[-1][0]}')
    print(f'Total: {sum}')
    print(f'Average: {sum/len(arr)}')

max_cummulative_sum(arr)

def track_sales(arr):
    max_sum = {}
    for i in range(len(arr)):
        sum = (int(arr[i][1]) * int(arr[i][2]))*2
        max_sum[i] =sum
    print(f'\nItem : {arr[max(max_sum, key=max_sum.get)][0]}')
    print(f'Total: {max(max_sum.values())}')
    print(f'Average: {max(max_sum.values())/len(arr)}')

track_sales(arr)