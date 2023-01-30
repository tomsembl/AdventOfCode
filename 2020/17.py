import copy

a="""..#..#..
.###..#.
#..##.#.
#.#.#.#.
.#..###.
.....#..
#...####
##....#."""
test=""".#.
..#
###"""
#a=test
actives={}
numCycles=6
for j,y in enumerate(a.splitlines()):
    for i,x in enumerate(y):
        if x == "#": 
            if i not in actives: actives[i] = {}
            actives[i][j] = [0]

def getNears(coords):
    x,y,z = coords
    nears=[]
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if not (x==i and (y==j and z==k)):
                    nears.append([i,j,k])
    return nears

def getQty(coords,getInactives=False):
    qty=0
    inactives=[]
    nears=getNears(coords)
    for i,j,k in nears:
        try: 
            actives[i][j].index(k)
            qty+=1
        except: 
            if getInactives: inactives.append([i,j,k])
    if getInactives: return qty, inactives
    return qty

for cycle in range(numCycles):
    newActives = []#copy.deepcopy(actives)
    newActivesDict = {}
    inactives=set()
    for x in actives:
        for y in actives[x]:
            for z in actives[x][y]:
                qty, inactives2 = getQty([x,y,z],True)
                for ina in inactives2: inactives.add(tuple(ina))
                if qty in [2,3]:
                    newActives.append([x,y,z])
    for x,y,z in inactives:
        qty = getQty([x,y,z])
        if qty == 3:
            newActives.append([x,y,z])

    for x,y,z in newActives:
        if x not in newActivesDict: newActivesDict[x]={}
        if y not in newActivesDict[x]: newActivesDict[x][y]=[]
        newActivesDict[x][y].append(z)
    actives = newActivesDict

total=0
for x in actives:
    for y in actives[x]:
        for z in actives[x][y]:
            total+=1
print(total)#part1