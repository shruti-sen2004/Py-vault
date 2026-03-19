# when lift moves up or down -> 2 sec/floor and stays at the target level -> 1sec
# if current and target floor same -> 1 sec
# return total time to complete all requests 

n = int(input())
f = list(map(int, input().split()))

curr_f= 0
time = 0
for i in f:
    if curr_f != i:
        time += abs(2*(i - curr_f)) +1
    else:
        time += 1
    curr_f = i
print(time)
