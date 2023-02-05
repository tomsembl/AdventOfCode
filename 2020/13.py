a="""1002461
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,521,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,601,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"""
test="""939
7,13,x,x,59,x,31,19"""
a=test
atBusStop=int(a.splitlines()[0])
busses=[int(x) for x in a.splitlines()[1].split(",") if x!="x"]
soonness=[]
for freq in busses:
    soonness.append([freq,freq-(atBusStop%freq)])
soonness.sort(key=lambda x: x[1])
soonest = soonness[0]
print(soonest[0]*soonest[1])#part1


busses=[[i,int(x)] for i,x in enumerate(a.splitlines()[1].split(",")) if x!="x"]
print(busses)
bussesDiff = [[bus[0]-busses[i-1][0], busses[i-1][1], bus[1]] for i,bus in enumerate(busses) if i != 0]

for diff,x,y in bussesDiff:
    print("x",x,"y",y,"diff",diff)
    xMultiple=1
    while (diff + x * xMultiple) % y != 0:
        xMultiple+=1
    yMultiple = (x * xMultiple + diff) // y
    print("xMultiple:", xMultiple, "yMultiple:", yMultiple)
    nextXmultiple = xMultiple+1
    while (diff + x * nextXmultiple) % y != 0:
        nextXmultiple+=1
    nextYmultiple = (x * nextXmultiple + diff) // y
    print("nextXmultiple:",nextXmultiple,"nextYmultiple:",nextYmultiple)