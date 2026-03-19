s = list(input())
nums = list(map(int, input().split(",")))

# key = s[3]
down = max(nums)-26
up = min(nums)-1

key = ''
for i in range(len(s)):
    x = ((ord(s[i])) - ord("A"))+1
    if x<up and x>down:
        key = s[i]

key_val = ord(key) - ord("A") +1
print(key_val)

new_string =""
for num in nums:
    new_string += chr((num-key_val)+ ord('A')-1)

print(new_string)
