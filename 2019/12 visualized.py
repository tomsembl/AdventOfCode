a="""<x=16, y=-8, z=13>
<x=4, y=10, z=10>
<x=17, y=-5, z=6>
<x=13, y=-3, z=0>"""
test="""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
#a=test
b=[{"pos":[int(y.split("=")[1]) for y in x[1:-1].split(", ")], "vel":[0,0,0]}for x in a.splitlines()]
nSteps=1000
#nSteps=10
n=4
print(b)
for step in range(nSteps):
    seen=[]
    for i in range(n):
        for j in range(n):
            if i==j or (min([j,i]),max([j,i])) in seen: continue
            seen.append( (min([j,i]),max([j,i])) )
            for axis in range(3):
                if b[i]["pos"][axis] == b[j]["pos"][axis]: continue
                dx = -1 if b[i]["pos"][axis] > b[j]["pos"][axis] else 1
                b[i]["vel"][axis] += dx
                b[j]["vel"][axis] -= dx
    for i in range(n):
        for axis in range(3):
            b[i]["pos"][axis] += b[i]["vel"][axis]

totalEnergy=0
for i in range(n):
    totalEnergy += sum([abs(x) for x in b[i]["pos"] ]) * sum([abs(x) for x in b[i]["vel"] ])

print(totalEnergy)
