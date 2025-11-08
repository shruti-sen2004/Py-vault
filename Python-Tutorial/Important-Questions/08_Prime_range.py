l = list(map(int, input().split()))

def isPrime(num):
	fact = 0
	i = 1
	while i<= num:
		if num %i ==0:
			fact +=1
		i +=1
	return fact

for i in range(l[0], l[1]+1):
	if isPrime(i) ==2 :
		if isPrime((i//10) + (i%10)) == 2:
			 print(i)
		