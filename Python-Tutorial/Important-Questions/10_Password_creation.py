pswd = input()
val = int(input())
s = ""

for i in pswd:
	if i.islower():
		i= chr((((ord(i) - ord('a'))+ val) %26) + ord('a'))
	elif i.isupper():
		i= chr((((ord(i) - ord('A'))+ val) %26) + ord('A'))
	elif i.isdigit():
		i = str((int(i)+ val)%10)
	elif i == '@':
		i = '#'
	elif i == '!':
		i = '@'
	else:
		pass
	s += i
print(s)	

