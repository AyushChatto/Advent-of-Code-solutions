a = []
for i in range(0, 16):
    temp = map(int, raw_input().strip().split())
    a.append(temp)

total = 0
for j in range(0, 16):
    highest = a[j][0]
    lowest = a[j][0]
    for k in range(0, len(a[j])):
        if(a[j][k] > highest):
            highest = a[j][k]
        elif(a[j][k] < lowest):
            lowest = a[j][k]
        else:
            pass
    total += (highest - lowest)
print total
