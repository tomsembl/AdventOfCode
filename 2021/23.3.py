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
  #A#D#C#A#
  #########"""
#a=test
part2Mid="""  #D#C#B#A#
  #D#B#A#C#"""
a="\n".join(a.splitlines()[:3]+[part2Mid]+a.splitlines()[3:]) #toggle for part 1 / 2
alphToNum = {"A":1,"B":2,"C":3,"D":4}
boxStateSplit=[[alphToNum[a.splitlines()[y][x]] for y in range(len(a.splitlines())-2,1,-1)] for x in range(3,10,2)]
h=len(boxStateSplit[0])
h4=h*4
boxState = [y for x in boxStateSplit for y in x]
hallState = [0,0,0,0,0,0,0]
graph = {(y:=j*h+i):{x:1 for x in [y-1,y+1] if j*h<=x<(j*h+h)}  for j in range(4) for i in range(h) } #room->room neighbours
[ graph[i*h+h-1].update( {x:2 for x in [h4+1+i,h4+i+2]}) for i in range(4) ] #room->hall neighbours
graph.update({ h4+i:{ x:(1 if all([z in [h4+0,h4+1,h4+5,h4+6] for z in [x,h4+i]]) else 2) for x in [h4+i-1,h4+i+1] if h4<=x<h4+7} for i in range(7) }) #hall->hall neighbours
[ graph[h4+i].update({x*h-1:2 for x in [i-1,i] if 0<x and x<5}) for i in range(7) ] #hall->room neighbours

for x in sorted(graph):
    print(x,graph[x])
print()

global distances
distances={}
def bfs(start):
    queue=[[start,[],0]]
    visited = set()
    while queue:
        node,path,cost=queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node != start:
                if ((start<h4) != (node<h4)) or start<h4:
                    distances[start][node] = [path,cost]
            for neighbour,cost2 in graph[node].items():
                queue.append([neighbour,path+[neighbour],cost+cost2])


for start in range(len(graph)):
    distances[start] = {}
    bfs(start)
    for destination in distances[start]:
        print(start,"->",destination, distances[start][destination])

endState=[x for x in range(1,5) for _ in range(h) ]
def validateHome(boxState,j):
    return not any([True for x in boxState[(j-1)*h:j*h] if x not in [0,j]])

def getHome(boxState,amphipod):
    homeBottom = (amphipod-1)*h
    for x in range(h):
        if boxState[homeBottom+x] == 0: return homeBottom+x
        if boxState[homeBottom+x] != amphipod: return -1
    return -1

def validatePath(state,path):
    for step in path:
        if state[step]: return False
    return True

def validateNode(state,node):
    return state[node] == 0

def cacheCheck(boxState,hallState,energy,returnHit=False):
    tbs,ths=tuple(boxState),tuple(hallState)
    if tbs in cache:
        if ths in cache[tbs]:
            if cache[tbs][ths]<=energy:
                if returnHit: return cache[tbs][ths]
                return False
        cache[tbs][ths]=energy
    else: 
        cache[tbs] = {}
        cache[tbs][ths]=energy
    return True

costs=[0,1,10,100,1000]
minEnergy=99999
queue=[[boxState,hallState,0]]
cache={}
iterations=0
while True:
    try: boxState, hallState, energy = queue.pop()
    except IndexError: break
    iterations+=1
    if not iterations % 100_000: print(iterations,len(queue))
    if energy >= minEnergy:continue
    if boxState == endState: 
        if energy < minEnergy:
            print("new minEnergy", energy)
            minEnergy = energy
        continue

    state = boxState + hallState
    for j in range(1,5):
        i=j*h-1
        while boxState[i]==0 and i>=0: 
            i-=1
        if i<0: continue
        amphipod = boxState[i]
        if amphipod == 0: continue
        if not validateHome(boxState, j):

            #go home -> hall
            possibleDestinations = []
            for x in distances[i][h4][0]: #left side of hall
                if validateNode(state,x):
                    if x>h4-1: possibleDestinations.append(x)
                else: break
            for x in distances[i][h4+6][0]: #right side of hall
                if validateNode(state,x):
                    if x>h4-1: possibleDestinations.append(x)
                else: break
            for x in possibleDestinations:
                path, cost = distances[i][x]
                newQueueItem = [boxState[:i]+[0]+boxState[i+1:], hallState[:x-h4]+[amphipod]+hallState[x-h4+1:], energy+cost*costs[amphipod]]
                if cacheCheck(*newQueueItem): queue.append(newQueueItem)

            #go home -> home
            if (home := getHome(boxState,amphipod)) == -1: continue
            path, cost = distances[i][home]
            if validatePath(state,path):
                newBoxState = boxState[:]
                newBoxState[i]=0
                newBoxState[home]=amphipod
                newQueueItem = [newBoxState, hallState, energy+cost*costs[amphipod]]
                if cacheCheck(*newQueueItem): queue.append(newQueueItem)

    for i2,amphipod2 in enumerate(hallState):
        if amphipod2 == 0: continue
        if (home := getHome(boxState,amphipod2)) == -1: continue

        #go hall -> home
        path, cost = distances[i2+h4][home]
        if validatePath(state,path):
            newQueueItem = [boxState[:home]+[amphipod2]+boxState[home+1:], hallState[:i2]+[0]+hallState[i2+1:], energy+cost*costs[amphipod2]]
            if cacheCheck(*newQueueItem): queue.append(newQueueItem)

print("Minimum Energy:", minEnergy) #part 2