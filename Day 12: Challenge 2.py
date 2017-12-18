master = []
n = input("How many programmes are there in this network? (Problem input has 2000)   ")
master2 = range(0,n)

def makeInt(x):
    if x[-1] == ",":
        return int(x[:-1])
    else:
        return int(x)


for i in range(0, n):
    a = raw_input().strip(',').split()
    master.append(map(makeInt, a[2:]))

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

groups = 0
meme = master[0]
pointer = 0
total = 0
scanner = 0

while total < n:
    while(pointer < len(meme)):
        temp = list(master[meme[pointer]])
        temp = diff(temp, meme)
        meme += temp
        pointer += 1
    total = len(meme)
    for k in range(0, len(meme)):
        if k in meme:
            pass
        else:
            pointer = k
            meme.append(k)
            print meme, "Cut off"
            groups += 1
            break


print groups + 1, "number of groups"

    

