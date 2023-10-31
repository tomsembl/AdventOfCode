a="""##.#.
#..#.
.....
....#
#.###"""
test="""....#
#..#.
#..##
..#..
#...."""
#a=test
from copy import deepcopy

nLevels = 110
reps=200
levels = {x:[[0 for _ in range(5)] for _ in range(5)] for x in range(-nLevels,nLevels+1)}
levels[0]=[[".#".index(x) for x in y] for y in a.splitlines()]
w,h = 5,5


def getAdj(levelID,x,y):
    if not  -nLevels < levelID < nLevels: return [0]
    neighs = {
         (1,2):[(4,y) for y in range(5)] #W
        ,(2,1):[(x,4) for x in range(5)] #N
        ,(3,2):[(0,y) for y in range(5)] #E
        ,(2,3):[(x,0) for x in range(5)] #S
    } 
    
    adjs = [levels[levelID][y+dy][x+dx] for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]] if -1 < y+dy < h and -1 < x+dx < w]
    for xx,yy in neighs:
        if (x,y) == (xx,yy):
            adjs.extend([levels[levelID-1][yyy][xxx] for xxx,yyy in neighs[(xx,yy)]])
        if (x,y) in neighs[(xx,yy)]:
            adjs.append(levels[levelID+1][yy][xx])
    return adjs
#conway's game of life, infinite fractal edition
for minute in range(reps):
    levelsCopy = deepcopy(levels)
    for levelID in levels:
        for j,y in enumerate(levels[levelID]):
            for i,x in enumerate(y):
                if (i,j) == (2,2): continue
                adj = getAdj(levelID,i,j)
                if x == 1: levelsCopy[levelID][j][i] = 1 if sum(adj) == 1 else 0
                if x == 0: levelsCopy[levelID][j][i] = 1 if sum(adj) in (1,2) else 0
    levels = levelsCopy
    # levelPrint = ["" for _ in range(5)]
    # for level in [levels[x] for x in range(-5,6)]:
    #     for j,y in enumerate(level):
    #         levelPrint[j] += "".join([str(x) for x in y])
    # for y in levelPrint:
    #     print("".join([str(x) for x in y]))
    # print()
print(sum([sum([sum(y) for y in levels[levelID]]) for levelID in levels])) #part 2