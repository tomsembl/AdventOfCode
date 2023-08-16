a="""depth: 9465
target: 13,704"""
depth= 9465
target= (13,704)

#test
# depth= 510
# target= (10,10)

tx,ty = target

erosionLevelMatrix=[[0 for x in range(tx+1)] for y in range(ty+1)]
geoIndexMatrix=[[0 for x in range(tx+1)] for y in range(ty+1)]
typeMatrix=[[0 for x in range(tx+1)] for y in range(ty+1)]

def getGeoIndex(c):
    if c in [(0,0),target]: return 0
    x,y = c
    if y == 0: return 16807 * x
    if x == 0: return 48271 * y
    return erosionLevelMatrix[y-1][x] * erosionLevelMatrix[y][x-1]

def getErosionLevel(c):
    x,y = c
    return (geoIndexMatrix[y][x] + depth) % 20183

def getType(c):
    x,y = c
    return erosionLevelMatrix[y][x] % 3

for x in range(tx+1):
    for y in range(ty+1):
        geoIndexMatrix[y][x] = getGeoIndex((x,y))
        erosionLevelMatrix[y][x] = getErosionLevel((x,y))
        typeMatrix[y][x] = getType((x,y))
        
# for row in typeMatrix:
#     print("".join([".=|"[x] for x in row]))

print(sum([sum(y) for y in typeMatrix])) #part 1

