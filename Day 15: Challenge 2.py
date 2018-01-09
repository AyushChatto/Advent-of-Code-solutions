a = 703
b = 516
count = 0
aS = []
bS = []
while len(bS) < (5 * (10 ** 6)):
    a = (a * 16807)%2147483647
    b = (b * 48271)%2147483647
    if a%4 == 0:
        aS.append(str(bin(a))[-16:])
    if b%8 == 0:
        bS.append(str(bin(b))[-16:])

#print len(aS), len(bS)
for j in range(0, min(len(aS), len(bS))):
    if aS[j] == bS[j]:
        count += 1
        #print j

print count, "This is the count"


