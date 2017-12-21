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
severity = 0
for i in range(0, n + 1):
    if grid[i] == 0:
        pass
    elif i % (2 * (grid[i] - 1)) == 0:
        severity += i*grid[i]
        #print i, grid[i], severity
    else:
        pass

print severity


