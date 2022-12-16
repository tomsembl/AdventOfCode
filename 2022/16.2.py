a="""Valve DJ has flow rate=0; tunnels lead to valves ZH, AA
Valve LP has flow rate=0; tunnels lead to valves AA, EE
Valve GT has flow rate=0; tunnels lead to valves FJ, AW
Valve RO has flow rate=5; tunnels lead to valves NO, FD, QV, BV
Valve PS has flow rate=0; tunnels lead to valves FY, UV
Valve QV has flow rate=0; tunnels lead to valves EB, RO
Valve MV has flow rate=0; tunnels lead to valves FL, EB
Valve RN has flow rate=0; tunnels lead to valves AW, LQ
Valve HF has flow rate=0; tunnels lead to valves QN, HW
Valve PY has flow rate=19; tunnel leads to valve SN
Valve AT has flow rate=0; tunnels lead to valves YQ, UY
Valve UY has flow rate=3; tunnels lead to valves KV, ID, AT, PB, PG
Valve YI has flow rate=0; tunnels lead to valves FL, FD
Valve EB has flow rate=8; tunnels lead to valves MV, GQ, QV
Valve ID has flow rate=0; tunnels lead to valves NO, UY
Valve FY has flow rate=15; tunnels lead to valves LQ, PS
Valve GQ has flow rate=0; tunnels lead to valves EB, KM
Valve HW has flow rate=0; tunnels lead to valves FJ, HF
Valve CQ has flow rate=17; tunnels lead to valves KM, GO
Valve AW has flow rate=20; tunnels lead to valves RN, GT, WH, MX
Valve BV has flow rate=0; tunnels lead to valves RO, ZH
Valve PB has flow rate=0; tunnels lead to valves UY, AA
Valve MX has flow rate=0; tunnels lead to valves AW, YG
Valve DE has flow rate=4; tunnels lead to valves MM, PZ, PG, DS, EP
Valve AA has flow rate=0; tunnels lead to valves EP, PB, LP, JT, DJ
Valve QN has flow rate=23; tunnels lead to valves SN, HF
Valve GO has flow rate=0; tunnels lead to valves CQ, MK
Valve PZ has flow rate=0; tunnels lead to valves IJ, DE
Valve PG has flow rate=0; tunnels lead to valves UY, DE
Valve FL has flow rate=18; tunnels lead to valves MV, YI
Valve DS has flow rate=0; tunnels lead to valves DE, ZH
Valve ZH has flow rate=11; tunnels lead to valves YQ, BV, DJ, DS, SB
Valve KV has flow rate=0; tunnels lead to valves UY, IJ
Valve UV has flow rate=9; tunnels lead to valves MM, PS, YG
Valve WH has flow rate=0; tunnels lead to valves JT, AW
Valve FD has flow rate=0; tunnels lead to valves YI, RO
Valve FJ has flow rate=24; tunnels lead to valves HW, GT
Valve JT has flow rate=0; tunnels lead to valves AA, WH
Valve SN has flow rate=0; tunnels lead to valves PY, QN
Valve KM has flow rate=0; tunnels lead to valves GQ, CQ
Valve LQ has flow rate=0; tunnels lead to valves RN, FY
Valve NO has flow rate=0; tunnels lead to valves ID, RO
Valve SB has flow rate=0; tunnels lead to valves ZH, IJ
Valve MK has flow rate=25; tunnel leads to valve GO
Valve YG has flow rate=0; tunnels lead to valves MX, UV
Valve IJ has flow rate=16; tunnels lead to valves EE, KV, PZ, SB
Valve EP has flow rate=0; tunnels lead to valves AA, DE
Valve MM has flow rate=0; tunnels lead to valves UV, DE
Valve YQ has flow rate=0; tunnels lead to valves AT, ZH
Valve EE has flow rate=0; tunnels lead to valves LP, IJ"""

test="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
#a=test
valves = {}
for line in a.splitlines():
    parts = line.split(";")
    valve = parts[0].split(" ")[1]
    flow_rate = int(parts[0].split("=")[1])
    tunnelsIndex = parts[1].split(" ").index("to")+2
    tunnels = [x.replace(",","") for x in parts[1].split(" ")[tunnelsIndex:] ]
    valves[valve] = {"flowRate": flow_rate, "leadsTo": tunnels}

#first DFS - to get distances
def bfs(start):
    queue = [[start, 0]]
    visited = set()
    while queue:
        node = queue.pop(0)
        distance = node[1]
        node = node[0]
        if node not in visited:
            visited.add(node)
            if node != start and valves[node]["flowRate"] != 0:
                valves[start]["distances"][node] = distance
            queue.extend([[x,distance+1] for x in valves[node]["leadsTo"]])

for valve in valves:
    valves[valve]["distances"] = {}
    bfs(valve)
    print(valves[valve]["distances"])

REMAININGMINUTES = 30
delay = 1
totalFlow = 0

#calculate the total flow of a path
def calcFlow(path):
    #get the distance between each pair in the path
    pathDistances = [0]
    for i in range(len(path)-1):
        node1, node2 = path[i], path[i+1]
        pathDistances.append(valves[node1]["distances"][node2])
    flow = 0
    #calculate the total flow over time
    for i,node in enumerate(path):
        flowRate = valves[node]["flowRate"]
        elapsedTime = sum(pathDistances[:i+1])
        delays = i * delay
        flow += flowRate * ( REMAININGMINUTES - elapsedTime - delays ) 
    #print()
    return flow


#second DFS tot try all possible paths
nonZeroFlowCount = sum([1 for x in valves if valves[x]["flowRate"] != 0])
start = "AA"
queue = [[start, 0, 0, []]]
maxFlow = 0
totalChecked = 0
while queue:
    if totalChecked % 10000 == 0: print(f"{totalChecked} iterations. {queue[0]}")
    totalChecked += 1
    node = queue.pop(0)
    node,time_spent, totalFlow, path = node
    flow = calcFlow(path)
    totalFlow = max(totalFlow, flow)
    if time_spent > REMAININGMINUTES: print("BAD")
    if len(path)==nonZeroFlowCount or time_spent == REMAININGMINUTES:
        path+=[node]
        totalFlow = calcFlow(path)
        if maxFlow < totalFlow:
            maxFlow = totalFlow
            print(totalFlow)
        continue
    candidates = list(valves[node]["distances"].keys())
    candidates.sort(key=lambda x: valves[x]["flowRate"], reverse=True)
    for neighbor in candidates:
        if neighbor in path:
            continue
        distance = valves[node]["distances"][neighbor]
        time_spent2 = time_spent + distance + delay 
        newPath = path+[node]
        if time_spent2 >= REMAININGMINUTES:
            newPath = path
            time_spent2 = REMAININGMINUTES
        queue.append([neighbor, time_spent2, totalFlow, newPath])
print(maxFlow)
#1906