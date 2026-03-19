n = input()
dig = list(map(int, str(n)))

def evendigits(dig): # checks for exactly 2 even nums
    count = 0
    for i in dig:
        if i % 2 == 0:
            count += 1
    
    return count

def sumdigits(dig): # calculates the sum of nums
    sum = 0
    for i in dig:
        sum += i  
    return sum

def norepeatdigit(dig): # checks if any repeated digits present
    j = 1
    for i in dig:
        if i in dig[j::]:
            return False
        j += 1
    return True

if len(n) != 4:
    print("INVALID!!")

else:
    if evendigits(dig) == 2:
        print("UNLOCKED by 1")
    elif sumdigits(dig) % 3 == 0:
        print("UNLOCKED by 2")
    elif norepeatdigit(dig) == True:
        print("UNLOCKED by 3")
    else:
        print("LOCKED")