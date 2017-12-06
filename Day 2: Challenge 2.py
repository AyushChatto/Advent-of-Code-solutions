a = []
for i in range(0, 16):
    temp = map(int, raw_input().strip().split())
    a.append(temp)

total = 0
for j in range(0, 16):
    for k1 in range(0, len(a[j])):
        for k2 in range(0, len(a[j])):
            if (k1 == k2):
                pass
            elif (a[j][k1] % a[j][k2] == 0):
                total += a[j][k1] / a[j][k2]
            else:
                pass
print total
