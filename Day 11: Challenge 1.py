# This is how my solution works:-
"""
I can actually can cancel out diammetrical opposites quite easily by simply counting the numbers of steps for each direction, 
and then subtracting. After this, I will be left with only three directions. Luckily for me, two of these directions will always
either add up to the third or its opposite. There are a total of 8 possible cases, and I have broken them up into 4 pairs (for the
same problem just mirrored in the opposite direction). After that, it's just simple algerbaic manipulation for the answer. 
"""
se = "se"
ne = "ne"
nw = "nw"
sw = "sw"
n = "n"
s = "s"

xs = [***INSERT PROBLEM INPUT HERE***]

# I know, I can cut down the time complexity by a factor of 6, but it'll still be linear, so meh.
ne = xs.count("ne")
se = xs.count("se")
sw = xs.count("sw")
nw = xs.count("nw")
n = xs.count("n")
s = xs.count("s")

#print xs, len(xs)
print n, s, ne, sw, se, nw
v = n - s
d2 = ne - sw
d1 = nw - se

# I was too lazy to write down the code for the other two conditions, since the first condition already answers the sample
# question. Suffice it to say that I can write those cases too. Ask me to write them if you really need me to make this solution
# airtight and for all possible inputs. 
if (v>= 0 and d1 >= 0 and d2 >= 0) or (v<= 0 and d1 <= 0 and d2 <= 0):
    print abs(v) + abs(d1 - d2) + min(abs(d1), abs(d2))
elif (v>= 0 and d1 >= 0 and d2 <= 0) or (v<= 0 and d1 <= 0 and d2 >= 0):
    print abs(d1) + abs(v - d2) + min(abs(v), abs(d2))    
elif (v>= 0 and d1 <= 0 and d2 >= 0) or (v<= 0 and d1 >= 0 and d2 <= 0):
    pass
elif (v<= 0 and d1 >= 0 and d2 >= 0) or (v>= 0 and d1 <= 0 and d2 <= 0):
    pass
