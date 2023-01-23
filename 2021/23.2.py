# indexes
# #############
# #01.2.3.4.56# (+8) = [8,9,10,11,12,13,14]
# ###1#3#5#7###
#   #0#2#4#6#
#   #########

a="""#############
#...........#
###A#D#B#D###
  #B#C#A#C#
  #########"""
test="""#############
#...........#
###B#C#B#D###
  #A#D#C#B#
  #A#D#C#B#
  #A#D#C#A#
  #########"""
test="""#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
a=test
alphToNum = {"A":1,"B":2,"C":3,"D":4}
boxStateSplit=[[alphToNum[a.splitlines()[y][x]] for y in range(len(a.splitlines())-2,1,-1)] for x in range(3,10,2)]
h=len(boxStateSplit[0])
boxState = [y for x in boxStateSplit for y in x]
hallState = [0,0,0,0,0,0,0]
graph = {i*h+j:{x:1 for x in [i-1,i+1] if 0<=x<(4*h)} for i in range(h) for j in range(4) }
print(graph)
graph={
    0:{1:1},
    1:{0:1,9:2,10:2},
    2:{3:1},
    3:{2:1,10:2,11:2},
    4:{5:1},
    5:{4:1,11:2,12:2},
    6:{7:1},
    7:{6:1,12:2,13:2},
    8:{9:1},
    9:{8:1,10:2,1:2},
    10:{9:2,11:2, h-1:2, 2*h-1:2},
    11:{10:2,12:2, 2*h-1:2, 3*h-1:2},
    12:{11:2,13:2, 3*h-1:2, 4*h-1:2},
    13:{12:2,14:1, 4*h-1:2},
    14:{13:1},
}
global distances
distances={}
distancesHome2Home={}
def bfs(start):
    queue=[[start,[],0]]
    visited = set()
    while queue:
        node,path,cost=queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node != start:
                if ((start<8) != (node<8)):
                    distances[start][node] = [path,cost]
                elif start<8:
                    distancesHome2Home[start][node] = [path,cost]
            for neighbour,cost2 in graph[node].items():
                queue.append([neighbour,path+[neighbour],cost+cost2])


for start in range(len(graph)):
    distances[start] = {}
    distancesHome2Home[start] = {}
    bfs(start)
    for destination in distances[start]:
        print(start,"->",destination, distances[start][destination])
    for destination in distancesHome2Home[start]:
        print(start,"->",destination, distancesHome2Home[start][destination])

endState=[1,1,2,2,3,3,4,4]
def validateHome(boxState,i,amphipod):
    if endState[i] == amphipod: 
        if i in [1,3,5,7]:
            return boxState[i-1] == amphipod
    return False

def getHome(boxState,amphipod):
    homeBottomLocation = 2*amphipod-2
    homeBottomContents = boxState[homeBottomLocation]
    if homeBottomContents==0: return homeBottomLocation
    if homeBottomContents==amphipod: return homeBottomLocation+1
    return None

def validatePath(state,path):
    for step in path:
        if state[step]: return False
    return True

def validateNode(state,node):
    return state[node] == 0

def cacheCheck(boxState,hallState,energy):
    tbs,ths=tuple(boxState),tuple(hallState)
    if tbs in cache:
        if ths in cache[tbs]:
            if cache[tbs][ths]<=energy:
                return False
        cache[tbs][ths]=energy
    else: 
        cache[tbs] = {}
        cache[tbs][ths]=energy
    return True

costs=[0,1,10,100,1000]
costMultiplier = lambda amphipod: costs[amphipod]
minEnergy=999999999999
queue=[[boxState,hallState,0]]
cache={}
iterations=0
hallCounts={i:{j:0 for j in range(5)} for i in range(7)}
while True:
    try: boxState, hallState, energy = queue.pop()
    except IndexError: break
    iterations+=1
    if not iterations % 100_000: print(iterations,len(queue))
    #if energy >= 100_000: continue
    if energy >= minEnergy:
        #print("energy too high")
        continue
    if boxState == endState: 
        #print("found endstate", energy)
        if energy < minEnergy:
            print("new minEnergy", energy)
            minEnergy = energy
        continue

    for i,x in enumerate(hallState): 
        hallCounts[i][x]+=1
    if not iterations % 1000: 
        for i in hallCounts:
            print(i+h*4,hallCounts[i])
        print()

    state = boxState + hallState
    for i,amphipod in enumerate(boxState):
        if amphipod == 0: continue
        if not validateHome(boxState, i, amphipod):

            #go home -> hall
            possibleDestinations = []
            for x in distances[i][8][0]: #left side of hall
                if validateNode(state,x):
                    if x>7: possibleDestinations.append(x)
                else: break
            for x in distances[i][14][0]: #right side of hall
                if validateNode(state,x):
                    if x>7: possibleDestinations.append(x)
                else: break
            for x in possibleDestinations:
                path, cost = distances[i][x]
                newQueueItem = [boxState[:i]+[0]+boxState[i+1:], hallState[:x-8]+[amphipod]+hallState[x-7:], energy+cost*costMultiplier(amphipod)]
                if cacheCheck(*newQueueItem): queue.append(newQueueItem)

            #go home -> home
            if (home := getHome(boxState,amphipod)):
                path, cost = distancesHome2Home[i][home]
                if validatePath(state,path):
                    newBoxState = boxState[:]
                    newBoxState[i]=0
                    newBoxState[home]=amphipod
                    newQueueItem = [newBoxState, hallState, energy+cost*costMultiplier(amphipod)]
                    if cacheCheck(*newQueueItem): queue.append(newQueueItem)

    for i2,amphipod2 in enumerate(hallState):
        if amphipod2 == 0: continue
        if not (home := getHome(boxState,amphipod2)): continue

        #go hall -> home
        path, cost = distances[i2+8][home]
        if validatePath(state,path):
            newQueueItem = [boxState[:home]+[amphipod2]+boxState[home+1:], hallState[:i2]+[0]+hallState[i2+1:], energy+cost*costMultiplier(amphipod2)]
            if cacheCheck(*newQueueItem): queue.append(newQueueItem)

print(minEnergy)
