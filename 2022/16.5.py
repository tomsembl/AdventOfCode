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

#first BFS - to get distances
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
    print(valve, valves[valve]["distances"])

REMAININGMINUTES = 26
delay = 1
totalFlow = 0

#calculate the total flow of a path
def calculateFlow(path):
    #get the distance between each pair in the path
    pathDistances = [0]
    for i in range(len(path)-1):
        valve1, valve2 = path[i], path[i+1]
        pathDistances.append(valves[valve1]["distances"][valve2])
    flow = 0
    #calculate the total flow over time for each valve
    for i,valve in enumerate(path):
        flowRate = valves[valve]["flowRate"]
        elapsedTime = sum(pathDistances[:i+1])
        delays = i * delay
        flow += flowRate * ( REMAININGMINUTES - elapsedTime - delays ) 
    #print()
    return flow


#second BFS tot try all possible paths
nonZeroFlowCount = sum([1 for x in valves if valves[x]["flowRate"] != 0])
print(f"nonZeroFlowCount: {nonZeroFlowCount}")
start = "AA"
queue = [{"nodes":[start,start], "timeSpents":[0,0], "paths":[[],[]]}]
maxFlow = 0
totalChecked = 0
while queue:
    noneExists = False
    if totalChecked % 1000 == 0: print(f"maxFlow:{maxFlow}. {totalChecked} iterations. queueLength={len(queue)}. queue[0]: {queue[0]}")
    totalChecked += 1
    node = queue.pop(0)
    nodes, timeSpents, paths = node["nodes"], node["timeSpents"], node["paths"]
    candidates = [[],[]]
    if None in nodes:
        if nodes == [None,None]: 
            totalFlow = calculateFlow(paths[0])+calculateFlow(paths[1])
            if maxFlow < totalFlow:
                maxFlow = totalFlow
                print(totalFlow , "BOTH NONE")
            continue
        noneIndex = nodes.index(None)
        notNoneIndex = 1 - noneIndex
        #what if theyre both None though??
        noneExists = True
        
    if noneExists:
        i = notNoneIndex
        candidates[i] = list(valves[nodes[i]]["distances"].keys())
        candidates[i] = [node for node in candidates[i] if node not in paths[0]+paths[1]+nodes]
        candidates[i].sort(key=lambda x: valves[x]["flowRate"], reverse=True)
        newTimeSpents = [REMAININGMINUTES,REMAININGMINUTES]
        newTimeSpents[notNoneIndex] = timeSpents[notNoneIndex] + valves[paths[notNoneIndex][-1]]["distances"][nodes[notNoneIndex]]
        outOfTimeBool = (newTimeSpents[0] == REMAININGMINUTES and newTimeSpents[1] == REMAININGMINUTES)
        noAvailableNodesBool = len(paths[0])+len(paths[1])+len([x for x in nodes if x])-2 == nonZeroFlowCount
        if noAvailableNodesBool or outOfTimeBool:
            newPaths = [paths[i] + ([ nodes[i]  ] if nodes[i] else []) for i in range(2)]
            totalFlow = calculateFlow(newPaths[0])+calculateFlow(newPaths[1])
            if maxFlow < totalFlow:
                maxFlow = totalFlow
                print(totalFlow , "noAvailableNodesBool" if noAvailableNodesBool else "OUT OF TIME" if outOfTimeBool else "both")
            continue


        for candidate0 in candidates[notNoneIndex]:
            newNodes =  [None,None]
            newNodes[notNoneIndex] = candidate0
            newTimeSpents = [REMAININGMINUTES,REMAININGMINUTES]
            newTimeSpents[notNoneIndex] = timeSpents[notNoneIndex] + valves[nodes[notNoneIndex]]["distances"][newNodes[notNoneIndex]]
            newPaths = [paths[i] +([ nodes[i] ]  if newNodes[i] else []) for i in range(2)]
            outOfTimeBool = (newTimeSpents[0] >= REMAININGMINUTES and newTimeSpents[1] >= REMAININGMINUTES)
            noAvailableNodesBool = len(newPaths[0])+len(newPaths[1])-2 == nonZeroFlowCount
            if noAvailableNodesBool or outOfTimeBool:
                totalFlow = calculateFlow(newPaths[0])+calculateFlow(newPaths[1])
                if maxFlow < totalFlow:
                    maxFlow = totalFlow
                    print(totalFlow , "noAvailableNodesBool" if noAvailableNodesBool else "OUT OF TIME" if outOfTimeBool else "both")
                continue
            for i in range(2):
                if newTimeSpents[i] >= REMAININGMINUTES:
                    newNodes[i] = None
                    newTimeSpents[i] = REMAININGMINUTES
                    newPaths[i] = paths[i]
            queue.append({"nodes":newNodes, "timeSpents":newTimeSpents, "paths":newPaths})

    else:
        for i in range(2):
            candidates[i] = list(valves[nodes[i]]["distances"].keys())
            candidates[i] = [node for node in candidates[i] if node not in paths[0]+paths[1]+nodes]
            candidates[i].sort(key=lambda x: valves[x]["flowRate"], reverse=True)
        
        if nodes==['AA', 'AA']:
            newTimeSpents = [0,0]
        else: newTimeSpents = [timeSpents[i] + valves[paths[i][-1]]["distances"][nodes[i]] for i in range(2)]
        outOfTimeBool = (newTimeSpents[0] == REMAININGMINUTES and newTimeSpents[1] == REMAININGMINUTES)
        noAvailableNodesBool = len(paths[0])+len(paths[1])+len([x for x in nodes if x])-2 == nonZeroFlowCount
        if noAvailableNodesBool or outOfTimeBool:
            newPaths = [paths[i] + ([ nodes[i]  ] if nodes[i] else []) for i in range(2)]
            totalFlow = calculateFlow(newPaths[0])+calculateFlow(newPaths[1])
            if maxFlow < totalFlow:
                maxFlow = totalFlow
                print(totalFlow , "noAvailableNodesBool" if noAvailableNodesBool else "OUT OF TIME" if outOfTimeBool else "both")
            continue


        for candidate0 in candidates[0]:
            
            candidates1 = [x for x in candidates[1] if x != candidate0]
            for candidate1 in candidates1:
                newNodes =  [candidate0,candidate1]
                newTimeSpents = [timeSpents[i] + valves[nodes[i]]["distances"][newNodes[i]] for i in range(2)]
                newPaths = [paths[i] + ([ nodes[i]  ] if nodes[i] else []) for i in range(2)]
                outOfTimeBool = (newTimeSpents[0] == REMAININGMINUTES and newTimeSpents[1] == REMAININGMINUTES)
                noAvailableNodesBool = len(newPaths[0])+len(newPaths[1])-2 == nonZeroFlowCount
                if noAvailableNodesBool or outOfTimeBool:
                    totalFlow = calculateFlow(newPaths[0])+calculateFlow(newPaths[1])
                    if maxFlow < totalFlow:
                        maxFlow = totalFlow
                        print(totalFlow , "noAvailableNodesBool" if noAvailableNodesBool else "OUT OF TIME" if outOfTimeBool else "both")
                    continue
                for i in range(2):
                    if newTimeSpents[i] >= REMAININGMINUTES:
                        newNodes[i] = None
                        newTimeSpents[i] = REMAININGMINUTES
                        newPaths[i] = paths[i]
                queue.append({"nodes":newNodes, "timeSpents":newTimeSpents, "paths":newPaths})


print(maxFlow)
#1713 @61000 #failed