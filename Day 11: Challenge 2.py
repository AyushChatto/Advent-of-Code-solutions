se = "se"
ne = "ne"
nw = "nw"
sw = "sw"
n = "n"
s = "s"

xs = [***COPY-PASTE THE PROBLEM INPUT HERE***]

maxdist = 0

for i in range(0, len(xs)):
    j = len(xs) - i - 1
    ne = xs[:j].count("ne")
    se = xs[:j].count("se")
    sw = xs[:j].count("sw")
    nw = xs[:j].count("nw")
    n = xs[:j].count("n")
    s = xs[:j].count("s")

    v = n - s
    d2 = ne - sw
    d1 = nw - se

    if (v>= 0 and d1 >= 0 and d2 >= 0) or (v<= 0 and d1 <= 0 and d2 <= 0):
        if abs(v) + abs(d1 - d2) + min(abs(d1), abs(d2)) > maxdist:
            #print "first"
            maxdist = abs(v) + abs(d1 - d2) + min(abs(d1), abs(d2))
            #print maxdist
        else:
            pass
            #print "passing 1"
    elif (v>= 0 and d1 >= 0 and d2 <= 0) or (v<= 0 and d1 <= 0 and d2 >= 0):
        if abs(d1) + abs(v + d2) + min(abs(v), abs(d2)) > maxdist:
            #print "Second"
            maxdist = abs(d1) + abs(v + d2) + min(abs(v), abs(d2))    
            #print maxdist
        else:
            pass
            #print "passing 2"
    elif (v>= 0 and d1 <= 0 and d2 >= 0) or (v<= 0 and d1 >= 0 and d2 <= 0):
        if abs(d2) + abs(v + d1) + min(abs(v), abs(d1)) > maxdist:
            #print "Third", v, d1, d2
            maxdist = abs(d2) + abs(v + d1) + min(abs(v), abs(d1))    
            #print maxdist
        else:
            pass
            #print "passing 3"
    elif (v<= 0 and d1 >= 0 and d2 >= 0) or (v>= 0 and d1 <= 0 and d2 <= 0):
        if abs(abs(v) - min(abs(d1), abs(d2)) + abs(d1 - d2)) > maxdist:
            #print "Fourth"
            maxdist = abs(abs(v) - min(abs(d1), abs(d2)) + abs(d1 - d2))  
            #print maxdist
        else:
            pass
            #print "passing 4"
print maxdist
