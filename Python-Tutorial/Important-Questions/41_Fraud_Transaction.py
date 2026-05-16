n = int(input("Enter the number of transactions: "))

data = {}
print("Enter transactions in the format: Sender Reciever Amount Transactionid")
for i in range(n):
    k = input().split()
    key = tuple([i]+k[0:2]+[round(float(k[2]),2)])
    val = int(k[-1])
    data[key] = val


keys_list = list(data.keys())
vals_list = list(data.values())


print("Fraud transaction found: Sender Reciever Amount Transactionid")

for i in range(n):
    for j in range(n):
        if i != j and i< j:
            if keys_list[i][1:] == keys_list[j][1:]:
                if 0<= vals_list[j] - vals_list[i]<=60:
                    print(*keys_list[j][1:], vals_list[j])


