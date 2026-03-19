# For greddy problems -> Sorting
w = list(map(int, input().split()))

if len(w)%2 != 0:   # as we cannot porm pairs with odd no.of elems
    print("Not possible")

else:
    w.sort()
    i = 0
    j = len(w)-1

    pairs = 0
    max = w[i] + w[j] # as all boxes must have same max weight that is (min + max)
    while(i<j):
        if w[i] + w[j] == max:
            pairs += 1
        else:
            pairs = -1
            break
        i += 1
        j -=1
    print(pairs)