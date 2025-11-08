def maxdiff(num: list[int])-> int:
	l,r = 0,1
	maxdis = 0
		
	while r < len(num):
		if num[l] < num [r]:
			distance = num[r] - num[l]
			maxdis = max(maxdis, distance)
		else:
			l = r 
		r += 1
	return maxdis

arr = [-3,-5,1,6,-7,8,11]
print(maxdiff(arr))