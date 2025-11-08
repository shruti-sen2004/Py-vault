nums = list(map(int,input().split(',')))
flag = 0

for num in nums:
	sum =0
	ognum = num
	while ognum >0:
		digit = ognum %10
		sum += digit ** len(str(num))
		ognum //= 10
	if sum == num:
		print(num, end =" ")
	flag = 1
		
if flag == 0: 
	print("No Armstrong numbers present")