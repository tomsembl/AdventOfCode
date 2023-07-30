SN=8199
test=18
size = 3
#SN=test

def getPowerLevel(x,y):
    rackID = x+10
    power = y * rackID
    power += SN
    power *= rackID
    hundreds = str(power)[-3:-2]
    power = 0 if hundreds=="" else int(hundreds)
    return power - 5

matrix = [[getPowerLevel(x+1,y+1) for x in range(300)] for y in range(300)]

def getCoords(size):
    maxTotal = -1000
    coords = ""
    matrix2 = [[sum([sum(y[i:i+size]) for y in matrix[j:j+size]]) for i in range(300-size+1)] for j in range(300-size+1)]
    for j,y in enumerate(matrix2):
        for i,x in enumerate(y):
            if x > maxTotal:
                maxTotal = x
                coords = f"{i+1},{j+1}"
    return coords,maxTotal

print(getCoords(3)[0]) #part 1

# maxTotal = -1000
# maxZ = None
# maxCoords = None
# for z in range(1,301):
#     coords,total = getCoords(z)
#     if total > maxTotal:
#         maxTotal = total
#         maxZ = z
#         maxCoords = coords
# print(f"{maxCoords}{maxZ}")

dic = {z:{y:{x:None for x in range(300)} for y in range(300)} for z in range(1,301)}
for z in range(1,301):
    #print(z)
    for j,y in enumerate(matrix):
        #if j+z > 300: continue
        for i,x in enumerate(y):
            if i+z > 300: continue
            dic[z][j][i] = sum(y[i:i+z])

def getCoords(size):
    #print(size)
    maxTotal = -1000
    coords = ""
    for j in range(300):
        if j+size > 300: continue
        for i in range(300):
            if i+size > 300: continue
            total = sum([dic[size][j][i] for j in range(j,j+size)])
            if total > maxTotal:
                maxTotal = total
                coords = f"{i+1},{j+1}"
    return coords,maxTotal

maxTotal = -1000
maxZ = None
maxCoords = None
for z in range(1,301):
    coords,total = getCoords(z)
    if total > maxTotal:
        maxTotal = total
        maxZ = z
        maxCoords = coords
print(f"{maxCoords},{maxZ}") #part 2
            