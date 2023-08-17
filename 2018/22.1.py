a="""depth: 9465
target: 13,704"""
depth= 9465
target= (13,704)

#test
#depth= 510
#target= (10,10)

tx,ty = target
buffer = 100

erosionLevelMatrix=[[0 for x in range(tx+buffer)] for y in range(ty+buffer)]
geoIndexMatrix=[[0 for x in range(tx+buffer)] for y in range(ty+buffer)]
typeMatrix=[[0 for x in range(tx+buffer)] for y in range(ty+buffer)]

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

for x in range(tx+buffer):
    for y in range(ty+buffer):
        geoIndexMatrix[y][x] = getGeoIndex((x,y))
        erosionLevelMatrix[y][x] = getErosionLevel((x,y))
        typeMatrix[y][x] = getType((x,y))
        
# 0,1,2 = rocky, wet, narrow
# tools: neither, torch, climbing
# allowedTools = [(1,2),(0,2),(0,1)]
import bisect
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
queue=[(0,0,0,1)]
seenPerTool=[{},{},{}]
minMinutes = 9999
while queue:
    x, y, minutes, tool = queue.pop(0)
    type = typeMatrix[y][x]
    if (x,y) == target:
        if tool != 1:
            minutes += 7
        if minutes < minMinutes:
            minMinutes = minutes
    #print(f"{minutes} ({x},{y}) type: {'.=|'[type]} tool: {'.=|'[tool]}")
    for nx,ny in [(x,y) for x,y in [(x+dx,y+dy) for dx,dy in dxdy] if tx+buffer > x >= 0 and ty+buffer > y >= 0]:
        nType = typeMatrix[ny][nx]
        nTool = {0,1,2}.difference({type,tool}).pop() if nType == tool else tool
        nMinutes = (8 if nType == tool else 1) + minutes
        c = (nx,ny)
        if c in seenPerTool[tool]:
            if nMinutes >= seenPerTool[tool][c]:
                continue
        seenPerTool[tool][c] = nMinutes
        bisect.insort(queue,(nx,ny,nMinutes,nTool),key = lambda x: x[2])
        #queue.append()
        #print(f"    {nMinutes} ({nx},{ny}) type: {'.=|'[nType]} tool: {'.=|'[nTool]}")
print(minMinutes) #part 2