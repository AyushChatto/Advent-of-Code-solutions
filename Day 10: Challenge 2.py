n = input("Number list length (256 for the official question)     ")
listOfNumbers = range(0,n)
currentPosition = 0
lengths = raw_input("What are the lengths? \n")
lengths = map(ord, list(lengths))
lengths += [17,31,73,47,23]
skipSize = 0

for i in range(0,64):
    for currentLength in lengths:
        if currentLength+currentPosition < n:
            temp = listOfNumbers[currentPosition: currentLength+currentPosition]
            temp.reverse()
            listOfNumbers[currentPosition: currentLength+currentPosition] = temp
        else:
            temp = listOfNumbers[currentPosition:]
            endLength = len(temp)
            temp += listOfNumbers[:currentLength - endLength] 
            temp.reverse()
            listOfNumbers[currentPosition:] = temp[:endLength]
            listOfNumbers[:currentLength - endLength] = temp[endLength:]
        if currentPosition+currentLength+skipSize < n:
            currentPosition += currentLength + skipSize
        else:
            currentPosition += currentLength + skipSize
            currentPosition = currentPosition % n     
        skipSize += 1

def xorOperator(xs):
    if len(xs) == 0:
        return 0
    else:
        return xs[0] ^ xorOperator(xs[1:])
ansList = []
for j in range(0,256, 16):
    ansList.append(xorOperator(listOfNumbers[j:j+16]))

ansList = map(hex, ansList)
print ansList
answer = ""
for k in range(0, len(ansList)):
    answer += ansList[k][2:]

print answer
