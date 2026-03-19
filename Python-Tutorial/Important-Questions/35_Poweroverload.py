# Count the no. of spikes that occur 
# if 3 consiqutive houses increasing power consumption -> spike+1
# return total spikes

power = list(map(int, input().split()))

i = 1
j = 2
spike = 0
for k in range(len(power)):
    if i != len(power) and j != len(power):
        if power[k] < power[i] and power[i] < power[j]:
            spike += 1
    i += 1
    j += 1

print(spike)