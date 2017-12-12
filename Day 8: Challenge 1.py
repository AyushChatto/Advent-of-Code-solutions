n = input("How many lines of commands?   ")
numbs = {}
commands = []
for i in range(0, n):
    temp = raw_input().strip().split()
    temp[2] = int(temp[2])
    temp[6] = int(temp[6])
    numbs[temp[0]] = 0
    commands.append(temp[0:])

for j in range(0, n):
    #print "here"
    if commands[j][1] == "inc":
        if commands[j][5] == ">":
            if numbs[commands[j][4]] > commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass

        elif commands[j][5] == "<":
            if numbs[commands[j][4]] < commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass

        elif commands[j][5] == "==":
            if numbs[commands[j][4]] == commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass


        elif commands[j][5] == "!=":
            if numbs[commands[j][4]] != commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass


        elif commands[j][5] == ">=":
            if numbs[commands[j][4]] >= commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass


        elif commands[j][5] == "<=":
            if numbs[commands[j][4]] <= commands[j][6] :
                numbs[commands[j][0]] += commands[j][2]
            else:
                pass

    else:
        if commands[j][5] == ">":
            if numbs[commands[j][4]] > commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass


        elif commands[j][5] == "<":
            if numbs[commands[j][4]] < commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass


        elif commands[j][5] == "==":
            if numbs[commands[j][4]] == commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass

        elif commands[j][5] == "!=":
            if numbs[commands[j][4]] != commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass

        elif commands[j][5] == ">=":
            if numbs[commands[j][4]] >= commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass

        elif commands[j][5] == "<=":
            if numbs[commands[j][4]] <= commands[j][6] :
                numbs[commands[j][0]] -= commands[j][2]
            else:
                pass

print max(numbs.values())
