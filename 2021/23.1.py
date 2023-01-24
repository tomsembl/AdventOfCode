# indexes
# #############   a   b   c   d  e
# #89.a.b.c.de#   10, 11, 12, 13,14
# ###1#3#5#7###
#   #0#2#4#6#
#   #########

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
boxState = [1,2,4,3,3,2,1,4]
hallState = [0,0,0,0,0,0,0]
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
    10:{9:2,11:2,1:2,3:2},
    11:{10:2,12:2,3:2,5:2},
    12:{11:2,13:2,5:2,7:2},
    13:{12:2,14:1,7:2},
    14:{13:1},
}
global distances
distances={}
distances2={}
def bfs(start):
    #isBox=start<8
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
                    distances2[start][node] = [path,cost]
            for neighbour,cost2 in graph[node].items():
                queue.append([neighbour,path+[neighbour],cost+cost2])


for start in range(15):
    distances[start] = {}
    distances2[start] = {}
    bfs(start)
    for destination in distances[start]:
        print(start,"->",destination, distances[start][destination])
    for destination in distances2[start]:
        print(start,"->",destination, distances2[start][destination])

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

def validatePath(boxState,hallState,path):
    state = boxState + hallState
    for step in path:
        if state[step]: return False
    return True

costMultiplier = lambda amphipod: 10**(amphipod-1)

minEnergy=999999999
queue=[[boxState,hallState,0]]
cache={}
iterations=0
while True:
    try: boxState, hallState, energy = queue.pop()
    except IndexError: break
    iterations+=1
    if not iterations % 100_000: print(iterations,len(queue))
    if boxState == endState: 
        if energy < minEnergy:
            print("new minEnergy", energy)
            minEnergy = energy
        continue
    tbs,ths=tuple(boxState),tuple(hallState)
    if tbs in cache:
        if ths in cache[tbs]:
            if cache[tbs][ths]<=energy:
                continue
        cache[tbs][ths]=energy
    else: 
        cache[tbs] = {}
        cache[tbs][ths]=energy
    for i,amphipod in enumerate(boxState):
        if amphipod == 0: continue
        if not validateHome(boxState, i, amphipod):
            #go home -> hall
            for x in distances[i]:
                path, cost = distances[i][x]
                if validatePath(boxState,hallState,path):
                    queue.append([boxState[:i]+[0]+boxState[i+1:], hallState[:x-8]+[amphipod]+hallState[x-7:], energy+cost*costMultiplier(amphipod)])
            #go home -> home
            if not (home := getHome(boxState,amphipod)): continue
            path, cost = distances2[i][home]
            if validatePath(boxState,hallState,path):
                newBoxState = boxState[:]
                newBoxState[i]=0
                newBoxState[home]=amphipod
                queue.append([newBoxState, hallState, energy+cost*costMultiplier(amphipod)])
    for i2,amphipod2 in enumerate(hallState):
        if amphipod2 == 0: continue
        if not (home := getHome(boxState,amphipod2)): continue
        #go hall -> home
        path, cost = distances[i2+8][home]
        if validatePath(boxState,hallState,path):
            queue.append([boxState[:home]+[amphipod2]+boxState[home+1:], hallState[:i2]+[0]+hallState[i2+1:], energy+cost*costMultiplier(amphipod2)])
print(minEnergy)
