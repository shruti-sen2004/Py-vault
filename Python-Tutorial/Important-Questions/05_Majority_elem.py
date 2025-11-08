from collections import Counter 

def max_appear(arr):
	elem = Counter(arr)
	for i in elem:
		if elem[i] >= len(arr)//3:
		 	return i
	
inp = input().split()
print(max_appear(inp))