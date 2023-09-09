a="""The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip."""
a=[["TG","TM","PG","SG"],
    ["PM","SM"],
    ["OG","OM","RG","RM"]
]
a=[[(0,0),(0,1),(1,0),(2,0)],
    [(1,1),(2,1)],
    [(3,0),(3,1),(4,0),(4,1)]
]
a=[[0,1,2,4,5,6,7,8],
    [3,5],
    [6,7,8,9],
    []
]
size = 7

test="""The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator."""
test=[["HM","LM"],
    ["HG"],
    ["LG"]
]
test=[[(0,1),(1,1)],
    [(0,0)],
    [(1,0)]
]
test=[[1,3],
    [0],
    [2],
    []
]
# a=test
# size = 2

from itertools import combinations

bits=[element*2+type_ for type_ in range(2) for element in range(size)]
print(bits)
e=0
#lift can only move 1 or 2 possible ways
floorOptions={0:[1], 1:[-1,1], 2:[-1,1], 3:[-1]}
#lift must have 1-2 things in it
#things in the lift must be able to survive in the next floor
#must not orphan a microchip with a different generator when leaving a floor
validFloors={}
def isValid(floor):
    floor = tuple(sorted(floor))
    if floor in validFloors:
        return validFloors[floor]
    for bit in floor:
        if bit&1:#is chip
            if bit-1 not in floor and any([True for bit in floor if bit&1==0]):
                validFloors[floor]=False
                return False
    validFloors[floor]=True
    return True

def state2(state):
    return state[:1] + tuple([tuple(sorted([y&1 for y in x])) for x in state[1:]])

start = tuple([0])+tuple([tuple(y) for y in a])
start2 = state2(start)

queue=[start]
seen={start2:0}
iterations = 0
minSteps=99999999
while queue:
    iterations += 1
    if iterations%100_000==0: print(iterations,queue[-1])
    state = queue.pop(0)
    floor, floors = state[0],state[1:]
    steps = seen[state2(state)]
    if len(floors[3]) == size*2:
        if steps < minSteps:
            minSteps = steps
        print(steps)
        continue
    moves2,moves1 = tuple(combinations(floors[floor],2)), tuple(combinations(floors[floor],1))
    for dir in floorOptions[floor]:
        if dir == -1:
            if all([not floor for floor in floors[:floor]]):
                continue #skip blank floor below
            moves = moves1
        else:
            moves = moves1+moves2
        for move in moves:
            newFloors = list(floors)
            newFloor = floors[floor+dir] + move
            oldFloor = tuple([x for x in floors[floor] if x not in move])
            if isValid(newFloor) and isValid(oldFloor):
                newFloors[floor+dir] = newFloor
                newFloors[floor] = oldFloor
                newState = (tuple([floor+dir]) + tuple(newFloors))
                newState2 = state2(newState)
                if steps + 1 >= minSteps: continue
                if newState2 not in seen:
                    seen[newState2] = steps + 1
                elif seen[newState2] <= steps + 1: continue
                queue.append(newState)
# generator = 0, chip = 1
# get same type chip from a generator +1
# get same type generator from a chip -1
            

#12207 too high