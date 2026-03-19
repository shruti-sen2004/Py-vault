# 3a2b3c -> aaabbcc
# 2ab4c -> aabcccc (if no number precending then print once)

code = input()

s =[]
letter =[]
i = 0
while (i < len(code)):
    if code[i].isdigit():
        s.append(code[i])
        letter.append(code[i+1])
        i += 2
    else:
        s.append(1)
        letter.append(code[i])
        i += 1

output =""
for i in range(len(letter)):
    output += letter[i] * int(s[i])
print(output)