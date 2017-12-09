total = 0
n = input("Enter number of lines in the problem (The AoC one has 512)   ")
print "Copy-paste the lines and hit enter    "
for i in range(0, n):
    a = raw_input().strip().split()
    for j in range(0, len(a)):
        a[j] = list(a[j])
        a[j].sort()
    for k in range(0, len(a)):
        if a.count(a[k]) > 1:
            break
        elif k == len(a) - 1:
            total += 1

print total
