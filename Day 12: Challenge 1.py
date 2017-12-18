master = []
n = input("How many programmes are there in this network? (Problem input has 2000)   ")

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

pointer = 0
meme = master[0]

while(pointer < len(meme)):
    temp = list(master[meme[pointer]])
    #print temp, "original temp"
    temp = diff(temp, meme)
    #print temp, "final temp"
    meme += temp
    pointer += 1
    print meme, pointer

