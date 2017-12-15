n = input("Number list length (256 for the official question)     ")
listOfNumbers = range(0,n)
currentPosition = 0
lengths = map(int, raw_input().split(','))
skipSize = 0
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
    print listOfNumbers[0:2]
