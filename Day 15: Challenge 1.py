a = 703
b = 516
count = 0
for i in range(0, 4 * (10**7)):
    a = (a * 16807)%2147483647
    b = (b * 48271)%2147483647
    abin = str(bin(a))[-16:]
    bbin = str(bin(b))[-16:]
    if abin == bbin:
        count += 1
        #print i
    else:
        pass

print count


