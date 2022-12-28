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

flowyValves = [x for x in valves if valves[x]["flowRate"] != 0]
for valve in flowyValves+["AA"]:
    valves[valve]["distances"] = {}
    bfs(valve)
    print(valve, valves[valve]["distances"])

#second BFS to try all possible paths
visited = set({})
valveIndexes = {x:i for i,x in enumerate(flowyValves)}
def tryPossibilities(time, currentValve, openValves, score):
    queue = [[time, currentValve, openValves, score]]
    visited = set({})
    maxFlow = 0
    totalChecked = 0
    while queue:
        time, currentValve, openValves, score = queue.pop(0)
        if (time, currentValve, openValves) in visited: continue
        visited.add((time, currentValve, openValves))
        for neighbour in valves[currentValve]["distances"]:
            bit = 1 << valveIndexes[neighbour]
            if openValves & bit: continue #if already open, skip
            newTime = time - valves[currentValve]["distances"][neighbour] - 1
            newScore = score + newTime * valves[neighbour]["flowRate"]
            if newTime <= 0: continue
            if newScore > maxFlow:
                maxFlow = newScore
                print("new max", maxFlow, "after", totalChecked, "iterations")
            queue.append([newTime, neighbour, openValves | bit, newScore])
        totalChecked += 1
    return maxFlow
#tryPossibilities(30, "AA", 0, 0) #part1


valveIndexes = {x:i for i,x in enumerate(flowyValves)}
def tryPossibilities2(times, currentValves, openValves, score):
    visited = {x:{y:{v:{vv:set({}) for vv in flowyValves+["AA"]} for v in flowyValves+["AA"]} for y in range(27)} for x in range(27)}
    queue = [[times, currentValves, openValves, score]]
    totalChecked = 0
    maxFlow = 0
    while queue:
        times, currentValves, openValves, score = queue.pop(0)
        time1,time2=times
        if time1>time2:
            time2,time1=times
            valve2,valve1=currentValves
        else:
            valve1,valve2=currentValves
        if openValves in visited[time1][time2][valve1][valve2]:
            continue
        visited[time1][time2][valve1][valve2].add(openValves)
        
        for neighbour1 in valves[valve1]["distances"]:
            bit1 = 1 << valveIndexes[neighbour1]
            if openValves & bit1: continue #if already open, skip
            newTime1 = time1 - valves[valve1]["distances"][neighbour1] - 1
            if newTime1 <= 0: continue
            for neighbour2 in valves[valve2]["distances"]:
                bit2 = 1 << valveIndexes[neighbour2]
                if openValves & bit2: continue
                if bit1 & bit2: continue
                newTime2 = time2 - valves[valve2]["distances"][neighbour2] - 1
                if newTime2 <= 0: continue
                newScore = score + newTime1 * valves[neighbour1]["flowRate"] + newTime2 * valves[neighbour2]["flowRate"]
                if newScore > maxFlow:
                    maxFlow = newScore
                    print("new max", maxFlow, "after", totalChecked, "iterations", bin(openValves))
                queue.append([(newTime1,newTime2), (neighbour1,neighbour2), (openValves | bit1) | bit2, newScore])
        totalChecked += 1
    return maxFlow
tryPossibilities2((26,26), ("AA","AA"), 0, 0)
#1713 failed @iteration 61000 
#1713            @iteration 33000 after sorting tweak 1
#1981 failed
#2036
#2049 failed
#2100 failed
#2173 failed
#2266 failed
#2415 failed
#2417 failed
#2500 failed