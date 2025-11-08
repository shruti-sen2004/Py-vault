def freq(num):
	num = sorted(num)[::-1]
	
	for i in range(len(num)):
		return max( num[0]*num[1]*num[2], num[0]* num[-1]*num[-2])

arr = list(map(int, input().split()))
print(freq(arr))