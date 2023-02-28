a="""<x=16, y=-8, z=13>
<x=4, y=10, z=10>
<x=17, y=-5, z=6>
<x=13, y=-3, z=0>"""
test="""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
# test="""<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>"""
#a=test
b=[{"pos":[int(y.split("=")[1]) for y in x[1:-1].split(", ")], "vel":[0,0,0]}for x in a.splitlines()]
nSteps=1000
#nSteps=10
n=4
def takeStep():
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

for step in range(nSteps): takeStep()

totalEnergy=0
for i in range(n):
    totalEnergy += sum([abs(x) for x in b[i]["pos"] ]) * sum([abs(x) for x in b[i]["vel"] ])
print(totalEnergy)#part1


b=[{"pos":[int(y.split("=")[1]) for y in x[1:-1].split(", ")], "vel":[0,0,0]}for x in a.splitlines()]
originalPos = [[x[z] for x in [x["pos"][:: ] for x in b]] for z in range(3)]
step=0
multiples={}
while len(multiples)<3:
    step+=1
    takeStep()
    for z in range(3):
        if [x["pos"][z] for x in b] == originalPos[z]:
            if z not in multiples: multiples[z]=step+1

def getLCM(array):
    lcms=[]
    lowerItems=[]
    for x in array:
        ms=[]
        y=2
        while y < x//2:
            if x%y==0:
                x//=y
                ms.append(y)
                y=2
                continue
            y+=1
        lowerItems.append(x)
        for z in set(ms):
            while ms.count(z) > lcms.count(z):
                lcms.append(z)
    lcm = 1
    for x in lcms: lcm*=x
    for x in lowerItems: lcm*=x
    return lcm

print(getLCM(multiples.values())) #part2
            

#2679502675707605 too high
#334945516288043 too low
#334945516288044