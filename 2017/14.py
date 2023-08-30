a="ugkiagan"
test="flqrgnkx"
#a=test
size=128
rows=[f"{a}-{i}" for i in range(size)]

def knotHash(a):
    b=[ord(x) for x in a] + [17, 31, 73, 47, 23]
    size=5
    size = 256
    c = list(range(size))
    pos = 0
    skip = 0
    for round in range(64):
        for length in b:
            slice = (c*2)[pos:pos+length]
            endPos = (pos+length)%size
            antiSlice = c[endPos:]+c[:pos] if endPos >= pos else c[endPos:pos]
            c = slice[::-1] + antiSlice
            c = (c*2)[size-pos:2*size-pos]
            pos += length + skip
            pos %= size
            skip += 1
    sparseHash = c
    denseSize = 16
    denseHash = []
    for i in range(denseSize):
        string1 = str(sparseHash[i*denseSize : (i+1)*denseSize])[1:-1].replace(", ","^")
        denseHash.append(eval(string1))
    denseHashHex = "".join([hex(x)[2:].zfill(2) for x in denseHash])
    return denseHashHex

def hexToBin(x): return bin(int(x,16))[2:].zfill(4)

matrix = [[int(y) for y in "".join([hexToBin(x) for x in knotHash(row)])] for row in rows]
print(sum([sum(row) for row in matrix])) #part 1

def isUsed(c):
    x,y = c
    if 0 <= x < size and 0 <= y < size:
        return bool(matrix[y][x])
    return False


groups = []
for y in range(size):
    for x in range(size):
        if not isUsed((x,y)): continue
        if any([(x,y) in group for group in groups]): continue
        seen = set()
        queue = [(x,y)]
        while queue:
            node = queue.pop(0)
            seen.add(node)
            nx,ny = node
            for dx,dy in [(1,0),(0,-1),(0,1),(-1,0)]:
                newNode = (nx+dx,ny+dy)
                if isUsed(newNode) and newNode not in seen:
                    queue.append(newNode)
        if len(seen) > 0: groups.append(seen)
print(len(groups))
# matrix2 = [[str(x) for x in y] for y in matrix]
# for group in groups:
#     for x,y in group:
#         matrix2[y][x] = "#"

# for row in matrix2:
#     print("".join(row)[:20].replace("0"," "))