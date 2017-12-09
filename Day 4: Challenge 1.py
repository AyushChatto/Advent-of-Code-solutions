total = 0
for i in range(0, 512):
    b = raw_input().strip().split()
    indicator = False
    if b != []:
        for j in range(0, len(b)):
            if b.count(b[j]) > 1:
                indicator = False
                break
            elif j == len(b) - 1:
                indicator = True
        if indicator == False:
            pass
        else:
            total += 1

    else:
        print total
        break
    
print total
