n = input("How many people in the tower?   ")
allNames = []
heldNames = []
for i in range(0, n):
    temp = list(raw_input().strip(", ").split())
    print temp
    allNames.append(temp[0])
    if len(temp) > 2:
        heldNames += temp[3:]
    else:
        pass

for i in range(0, len(allNames)):
    if allNames[i] in heldNames or allNames[i] +"," in heldNames:
        pass
    else:
        print allNames[i]
        pass

