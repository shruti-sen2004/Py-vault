import math
def round_off_5(num):
    if num % 5 == 1 or num % 5 == 2 :
           #num = math.floor(num/5)*5
           num = num - (num%5)
    elif num % 5 == 3 or num % 5 == 4 :
            #num = math.ceil(num/5)*5
            num = num + 5 - (num %5)
    else:
        pass 
    return num

def price_calculate(n, prices:list[float]):
    t = 0                # together_sum
    s = 0                # seperate_sum
    for x in prices:
        t += x
        s += round_off_5(x)


    return s - round_off_5(t)
    

print(price_calculate(3,[12,17,23]))


