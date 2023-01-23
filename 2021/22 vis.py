a="""on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""
# a="""on x=0..2,y=1..2,z=1..2
# of x=1..1,y=0..3,z=0..3"""
# a="""on x=0..2,y=0..2,z=1..1
# off x=0..2,y=0..2,z=0..2"""
b=    [[[int(z) for z in y[2:].split("..")] for y in x.split()[1].split(",")]+[x.split()[0]=="on",i] for i,x in enumerate(a.splitlines())]
queue=[[[int(z) for z in y[2:].split("..")] for y in x.split()[1].split(",")]+[x.split()[0]=="on",i] for i,x in enumerate(a.splitlines())]
#get the minimum and maximum int values from queue
minn,maxx=min([min([min(x) for x in y[:3]]) for y in queue]),max([max([max(x) for x in y[:3]]) for y in queue])+1
global cubes
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

animationFrames=[]
prevCube=0
while queue:
    cube1 = queue.pop(0) 
    animationFrames.append([[cube1],cubes])
    # if cube1[4]!=prevCube and b[prevCube][3]:
    #     cubes=[x for x in cubes if x[4]!=prevCube] #remove all cube1 splits from cubes
    #     cubes.append(b[prevCube])
    #     prevCube=cube1[4]
    hasCollisions = False
    breakFlag=False
    for j,cube2 in enumerate(cubes):
        if breakFlag: break
        if cube1[:3]==cube2[:3]:
            cubes=cubes[:j]+cubes[j+1:] #erase duplicate
            break #skip edgechecks etc

        collides, edgeChecks = collisionCheck(cube1,cube2)
        if not collides: continue

        hasCollisions = True
        print("collision",cube1,cube2,edgeChecks)
        # for edgeCheck in edgeChecks: #remove cube2 in some cases
        #     if edgeCheck in [[0,0,1,0],[1,0,1,1],[1,0,1,0]]: 
        #         cubes=cubes[:j]+cubes[j+1:] 
        #         break
        cube2Deleted = False
        for i in range(3):
            edgeCheck = edgeChecks[i]
            p,q = cube1[i]
            r,s = cube2[i]
            if p==r and q==s: continue #both edges exactly match for this axis (already split along this axis previously)
            type = [[0,0,1,0],[1,0,1,1],[1,0,1,0],[0,0,1,1]].index(edgeCheck)
            #split
            newQueue,newCubes=[],[]
            cubes=cubes[:j]+cubes[j+1:] 
            if type==0: 
                #prqs
                if r!=p: newQueue.append(cube1[:i] + [[p,r-1]] + cube1[i+1:])
                newQueue.append(cube1[:i] + [[r,q]]   + cube1[i+1:])
                newCubes.append(cube2[:i] + [[r,q]] + cube2[i+1:])
                if q!=s: newCubes.append(cube2[:i] + [[q+1,s]] + cube2[i+1:])
            if type==1:
                #rpsq
                if r!=p: newCubes.append(cube2[:i] + [[r,p-1]] + cube2[i+1:])
                newCubes.append(cube2[:i] + [[p,s]] + cube2[i+1:])
                newQueue.append(cube1[:i] + [[p,s]] + cube1[i+1:])
                if q!=s: newQueue.append(cube1[:i] + [[s+1,q]]   + cube1[i+1:])
            if type==2:
                #rpqs
                newQueue.append(cube1)
                if r!=p: newCubes.append(cube2[:i] + [[r,p-1]] + cube2[i+1:])
                newCubes.append(cube2[:i] + [[p,q]] + cube2[i+1:])
                if q!=s: newCubes.append(cube2[:i] + [[q+1,s]] + cube2[i+1:])
            if type==3: 
                #prsq
                newCubes.append(cube2)
                if r!=p: newQueue.append(cube1[:i] + [[p,r-1]] + cube1[i+1:])
                newQueue.append(cube1[:i] + [[r,s]] + cube1[i+1:])
                if q!=s: newQueue.append(cube1[:i] + [[s+1,q]] + cube1[i+1:])

            for nq in newQueue: queue.insert(0,nq)
            for nc in newCubes: cubes.append(nc)
            #print(f"{'xyz'[i]} axis slice. {['left','right','inner','outer'][type]}. newqueue={newQueue}. newcubes={newCubes}")
            breakFlag=True
            break#do the others later, in the queue

    if not hasCollisions and cube1[3]: cubes.append(cube1)

animationFrames.append([[],cubes])

totalVolume=0
for cube in cubes:
    total=1
    for x,y in cube[:3]:
        total*= y-x+1
    totalVolume+=total
    #print(cube)
print(totalVolume)
#[p, q, r, s]        
#[0, 0, 0, 0] left, right,   no collision. insert cube1 if no other collisions
#[1, 1, 1, 1] right, left,   no collision. insert cube1 if no other collisions
#[0, 0, 1, 0] left, right,      collision. split each  into 2. delete cube2. insert 2x new cube1 in queue, append 2x new cube2 in cubes
#[1, 0, 1, 1] right, left,      collision. split each  into 2. delete cube2. insert 2x new cube1 in queue, append 2x new cube2 in cubes
#[1, 0, 1, 0] inside, outside,  collision. split cube2 into 3. delete cube2. insert cube1 in queue,        append 3x new cube2 in cubes
#[0, 0, 1, 1] outside, inside,  collision. split cube1 into 3.               insert 3x new cube1 in queue.

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint
import numpy as np
fig = plt.figure()
x, y, z = np.indices((maxx for _ in range(3)))
colours = [[0,1,0,0.4],[0,0,1,0.4],[1,1,0,0.4],[0,1,1,0.4],[1,1,1,0.4],[0.0,0,0.4]]
def update(n):    
    try: queue2,cubes2 = animationFrames[n]
    except: 
        ani.pause()
        return
    init()    
    for ii in range(len(queue2)): 
        a = [x for y in queue2[ii][:3] for x in y]
        ax.voxels((x >= a[0]) & (x <= a[1]) & (y >= a[2]) & (y <= a[3]) & (z >= a[4]) & (z <= a[5]), facecolors=[1,0,0]+[0.6], edgecolors=[1,1,1, 0.05])
    for ii,a in enumerate([[x for y in z[:3] for x in y] for z in cubes2]):
        ax.voxels((x >= a[0]) & (x <= a[1]) & (y >= a[2]) & (y <= a[3]) & (z >= a[4]) & (z <= a[5]), facecolors=colours[ii%len(colours)], edgecolors=[1,1,1, 0.05])

def init():
    global ax
    ax = fig.add_subplot(111, projection='3d')
    ax.axes.set_xlim3d(left=minn, right=maxx)
    ax.axes.set_ylim3d(bottom=minn, top=maxx) 
    ax.axes.set_zlim3d(bottom=minn, top=maxx) 

ani = FuncAnimation(fig, update, frames=len(animationFrames), interval=500, repeat=False, init_func=init)
plt.show()