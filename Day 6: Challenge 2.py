print( "Copy-paste the input blocks to be reallocated")
a = map(int, raw_input().strip().split())
steps = 0
memes = []
while True:
    if a not in memes:
        c = a[:]
        memes.append(c)
        b = max(a)
        bi = a.index(b)
        a[bi] = 0
        bi += 1
        while b > 0:
            if bi == len(a):
                bi = 0
            else:
                a[bi] += 1
                bi += 1
                b -= 1
                #print a, memes
        steps += 1
    else:
        break

print len(memes) - memes.index(a) 

    
