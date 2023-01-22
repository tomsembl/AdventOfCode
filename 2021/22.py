a="""on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""
b=[[[int(z) for z in y[2:].split("..")] for y in x.split()[1].split(",")]+[x.split()[0]=="on"] for x in a.splitlines()]
cubes=[]
def collisionCheck(cube1,cube2):
    collides,edgeChecks=True,[]
    for i in range(3):
        p,q = cube1[i]
        r,s = cube2[i]
        edgeCheck = [int(x) for x in [p>=r, p>s, q>=r, q>s]]
        edgeChecks.append(edgeCheck)
        if sum(edgeCheck) in [0,4]: collides=False
    return collides, edgeChecks
        
for i,x in enumerate(b):
    for j,y in enumerate(b):
        if i==j: continue
        print(i,j,collisionCheck(x,y))