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

#traverse graph from all nodes and find the path length to every other node
# BFS function to traverse the graph
def bfs(start):
    queue = [[start, 0]]
    visited = set()
    while queue:
        node = queue.pop(0)
        distance = node[1]
        node = node[0]
        if node not in visited:
            visited.add(node)
            if node != start:
                valves[start]["distances"][node] = distance
            queue.extend([[x,distance+1] for x in valves[node]["leadsTo"]])

for valve in valves:
    valves[valve]["distances"] = {}
    bfs(valve)
        
for valve in valves:
    print(valve,valves[valve]["distances"])

remainingMinutes = 30
delay = 1
currentlyFlowing = []
totalFlow = 0
def goToNextBest(start):
    print(start)
    global remainingMinutes, currentlyFlowing, totalFlow
    if remainingMinutes <= 0:    
        return
    otherNodes = [x for x in valves if x != start and x not in currentlyFlowing]
    if len(otherNodes) == 0:
        print("no other nodes")
        return
    worths = []
    for x in otherNodes:
        travelTime, flow = valves[start]["distances"][x], valves[x]["flowRate"]
        worths.append([(remainingMinutes - travelTime - delay) * flow, x, travelTime])
    worths.sort(reverse=True)
    worthinessScore, worthyNode, wnTime =  worths[0]
    timeSpent = wnTime + delay
    #remainingMinutes -= timeSpent
    for minute in range((timeSpent if timeSpent <= remainingMinutes else  remainingMinutes)):
        minuteFlow = sum([valves[node]["flowRate"] for node in currentlyFlowing])
        remainingMinutes -= 1
        print("remainingMinutes",remainingMinutes, "currentlyFlowing",currentlyFlowing, "minuteFlow",minuteFlow)
        totalFlow += minuteFlow
    currentlyFlowing.append( worthyNode )
    return goToNextBest(worths[0][1])
goToNextBest("AA")
print(totalFlow)


# minutes = 30
# visited = []
# def openValve(valveName):
#     visited.append(valveName)
#     valve = valves[valveName]
#     print(valve)
#     for leadsTo in valve["leadsTo"]:
#         nextValve = valves[leadsTo]
#         if nextValve["flowRate"] != 0 and leadsTo not in visited:
#             openValve(valves[leadsTo])
# openValve("AA")
# for minute in range(minutes):

#     minutes -= 1