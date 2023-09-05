a="""R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"""
test="""R2, L3"""
test="""R2, R2, R2"""
test="""R5, L5, R5, R3"""
test="""R8, R4, R4, R8"""
#a=test
def manhattan(x,y): return abs(0+x) + abs(0+y)
b=[(x[0],int(x[1:])) for x in a.split(", ")]
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
def part(p):
    x,y,dir=0,0,0
    seen=set((0,0))
    for turn,dist in b:
        dir += -1 if turn=="L" else 1
        dir %= 4
        dx,dy = dirs[dir]
        for walk in range(dist):
            x,y = x+dx,y+dy
            if (x,y) in seen and p==2:
                print(manhattan(x,y))
                return
            seen.add((x,y))
    if p == 1: print(manhattan(x,y))
part(1)
part(2)