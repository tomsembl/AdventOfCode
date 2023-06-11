a="""162, 168
86, 253
288, 359
290, 219
145, 343
41, 301
91, 214
166, 260
349, 353
178, 50
56, 79
273, 104
173, 118
165, 47
284, 235
153, 69
116, 153
276, 325
170, 58
211, 328
238, 346
333, 299
119, 328
173, 289
44, 223
241, 161
225, 159
266, 209
293, 95
89, 86
281, 289
50, 253
75, 347
298, 241
88, 158
40, 338
291, 156
330, 88
349, 289
165, 102
232, 131
338, 191
178, 335
318, 107
335, 339
153, 156
88, 119
163, 268
159, 183
162, 134"""
test="""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
#a=test
b=[[int(x.strip()) for x in y.split(",")] for y in a.splitlines()]
maxX=max(b,key=lambda x:x[0])[0]
maxY=max(b,key=lambda x:x[1])[1]
grid=[[" " for x in range(maxX+1)] for y in range(maxY+1)]

def manhattanDistance(xy,xxyy):
    x,y=xy
    xx,yy=xxyy
    return abs(x-xx) + abs(y-yy)

for y, row in enumerate(grid):
    for x in range(len(row)):
        distances = [(i,manhattanDistance([x,y],location)) for i,location in enumerate(b)]
        minDist = min(distances,key=lambda x:x[1])
        if [x[1] for x in distances].count(minDist[1]) == 1:
            grid[y][x] = minDist[0]

largestArea = 0
for i in range(len(b)):
    if i in grid[0]+grid[-1]: continue #top bottom
    if i in [y[0] for y in grid]+[y[-1] for y in grid]: continue #left right
    area = sum([y.count(i) for y in grid])
    if area > largestArea: largestArea = area
print(largestArea) #part1

safeArea = 0
for y, row in enumerate(grid):
    for x in range(len(row)):
        distances = [manhattanDistance([x,y],location) for location in b]
        if sum(distances) < 10_000:safeArea+=1
print(safeArea)


