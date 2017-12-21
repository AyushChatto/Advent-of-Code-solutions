n = input("How many layers are there? (90 in the problem)  ")
print "Enter all the values and hit enter twice after the last one"
grid = range(0, n + 1)

def f(x):
    return 0

grid = map(f, grid)

try:
    while True:
        temp = map(int, raw_input().strip().split(':'))
        #print temp, "this is temp"
        if len(temp) != 0:
            grid[temp[0]] = temp[1]
        else:
            break
except:
    pass

#print grid
#severity = 0
delay = 0
j = 0

def gotHit(layer, rangeOfDrone, delayTime):
    return (layer + delayTime) % (2 * (grid[j] - 1)) == 0

while j < n+1:
    for j in range(0, n + 1):
        if grid[j] == 0:
            pass
        elif gotHit(j, grid[j], delay):
            #severity += i*grid[i]
            print "doesn't work for delay =", delay
            delay += 1
            break
            #print i, grid[i], severity
        else:
            pass

 
print delay


