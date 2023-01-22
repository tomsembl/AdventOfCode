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
        if sum(edgeCheck) in [0,4]: 
            collides=False
            return collides, edgeChecks
    return collides, edgeChecks
        
for i,cube1 in enumerate(b):
    hasCollisions = False
    for j,cube2 in enumerate(cubes):
        if i==j: continue
        collides, edgeChecks = collisionCheck(cube1,cube2)
        if not collides: continue
        hasCollisions = True
        print("collision",i,j,edgeChecks)
        for p,q,r,s in edgeChecks: #remove cube2 in some cases
            if [p,q,r,s] in [[0, 0, 1, 0],[1, 0, 1, 1],[0, 0, 1, 1]]: cubes=cubes[:j]+cubes[j+1:]
        cubeQueue=[]
        while cubeQueue:
    if not hasCollisions: cubes.append(cube1)
for cube in cubes:
    print(cube)
#[p, q, r, s]        
#[0, 0, 0, 0] left, right,   no collision. insert cube1 if no other collisions
#[1, 1, 1, 1] right, left,   no collision. insert cube1 if no other collisions
#[0, 0, 1, 0] left, right,      collision. delete cube2. split each into 2
#[1, 0, 1, 1] right, left,      collision. delete cube2. split each into 2
#[1, 0, 1, 0] inside, outside,  collision. split cube2 into 3. insert 4
#[0, 0, 1, 1] outside, inside,  collision. split cube1 into 3. delete cube2, insert 4

# for p,q,r,s in [[-2,-1,1,2],[4,5,1,2],[0,1,1,2],[1,2,0,1],[1,3,0,4],[0,4,1,3]]:
#     edgeCheck = [int(x) for x in [p>=r, p>s, q>=r, q>s]]
#     print(p,q,r,s,edgeCheck)