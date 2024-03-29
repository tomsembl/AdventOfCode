a="""addx 1
noop
noop
addx 4
addx 5
addx -2
addx 19
addx -12
addx 3
addx -2
addx 4
noop
noop
noop
addx 3
addx -8
addx 15
addx 1
noop
noop
addx 6
addx -1
noop
addx -38
noop
addx 10
addx -5
noop
addx 3
addx 2
addx 7
noop
noop
addx 3
noop
addx 2
addx 3
addx -2
addx 2
addx 7
noop
noop
addx 9
noop
addx -12
noop
addx 11
addx -38
noop
noop
noop
addx 5
addx 5
noop
noop
noop
addx 3
addx -12
addx 14
noop
addx 1
addx 3
addx 1
addx 5
addx 4
addx 1
noop
noop
noop
noop
noop
addx -9
addx 17
addx -39
addx 38
addx -8
addx -26
addx 3
addx 4
addx 16
noop
addx -11
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
addx 13
addx -8
noop
addx 7
addx -5
addx 8
addx -40
addx 16
addx -9
noop
addx -7
addx 8
addx 2
addx 7
noop
noop
addx -15
addx 16
addx 2
addx 5
addx 2
addx -20
addx 12
addx 11
addx 8
addx -1
addx 3
noop
addx -39
addx 2
noop
addx 5
noop
noop
noop
addx 4
addx 1
noop
noop
addx 2
addx 5
addx 2
addx 1
addx 4
addx -1
addx 2
noop
addx 2
noop
addx 8
noop
noop
noop
addx -10
noop
noop"""

test="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

dic = {"noop":1,"addx":2}
instructions = [[dic[x] if x in dic.keys() else int(x) for x in y.split(" ")] for y in a.splitlines()]
instructions = [(x+[0])[:2] for x in instructions]
x, cycleCount, totalSignalStrength = 1, 1, 0

for numCycles, xIncrement in instructions:
    for opNum in range(numCycles):
        cycleCount += 1
        x += xIncrement if opNum == 1 else 0
        if cycleCount in range(20,221,40):
            signalStrength = x * cycleCount
            totalSignalStrength += signalStrength

print(totalSignalStrength) #part1

x, cycleCount, text, width, height = 1, 0, "", 40, 6

for numCycles, xIncrement in instructions:
    for opNum in range(numCycles):
        text += "█" if cycleCount % width in range(x-1,x+2) else "░" #draw pixel
        x += xIncrement if opNum == 1 else 0 #move sprite
        cycleCount += 1

for x in range(0, width*height, width):
    print(text[x:x+40]) #part2