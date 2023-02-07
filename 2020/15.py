a=[6,13,1,15,2,0]
test=[0,3,6]
#a=test
totalIterations = 2020 #part1
totalIterations = 30000000 #part2
PosDict={}
countDict={}
diffDict={}
for i,x in enumerate(a):
    PosDict[x]=i
    countDict[x] = 1
for i in range(len(a),totalIterations):
    if not i%100_000: print(i)
    if countDict[x] == 1: x = 0
    else: x = diffDict[x]

    if x not in countDict:countDict[x]=0
    countDict[x] += 1
    diffDict[x] = i - PosDict[x] if x in PosDict else 0
    PosDict[x] = i
print(x)
