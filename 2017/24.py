a="""42/37
28/28
29/25
45/8
35/23
49/20
44/4
15/33
14/19
31/44
39/14
25/17
34/34
38/42
8/42
15/28
0/7
49/12
18/36
45/45
28/7
30/43
23/41
0/35
18/9
3/31
20/31
10/40
0/22
1/23
20/47
38/36
15/8
34/32
30/30
30/44
19/28
46/15
34/50
40/20
27/39
3/14
43/45
50/42
1/33
6/39
46/44
22/35
15/20
43/31
23/23
19/27
47/15
43/43
25/36
26/38
1/10"""
test="""0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
#a=test
ports=[(0,0)]+[tuple([int(y) for y in x.split("/")]) for x in a.splitlines()]
allPortIDs = set(range(len(ports)))

queue=[(0,{0},0)]
maximum = 0
while queue:
    freePort, usedPorts, total = queue.pop()
    if total > maximum:
        maximum = total
    availablePorts = allPortIDs.difference(usedPorts)
    for portID in availablePorts:
        port = ports[portID]
        if port[0] == freePort or port[1] == freePort:
            queue.append((port[0] if port[1] == freePort else port[1], usedPorts.union({portID}), total+sum(port)))
print(maximum)#part 1

queue=[(0,{0},0)]
maximumStrength = 0
maximumLength = 0
while queue:
    freePort, usedPorts, total = queue.pop()
    if len(usedPorts) >= maximumLength:
        maximumLength = len(usedPorts)
        if total > maximumStrength:
            maximumStrength = total
    availablePorts = allPortIDs.difference(usedPorts)
    for portID in availablePorts:
        port = ports[portID]
        if port[0] == freePort or port[1] == freePort:
            queue.append((port[0] if port[1] == freePort else port[1], usedPorts.union({portID}), total+sum(port)))
print(maximumStrength)#part 2