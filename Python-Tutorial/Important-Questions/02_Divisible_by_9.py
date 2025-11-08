num = int (input())

## M-1
if 100<= num <= 900:
	if num % 9 ==0 :
		print("Divisible by 9")
	else:
		print("Not Divisible by 9")

## M-2
res = { True: "Divisible" , False: "not divisible"}[num %9 ==0]
print(res)