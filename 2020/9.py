a=""""""
test=""".#.
..#
###"""
a=test
dic={}
#active=[]
#b=[[x for i,x in enumerate(y)] for j,y in enumerate(a.splitlines())]

def numNeighbs(coords):
    x,y,z = coords
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                print(i,j,k)

for j,y in enumerate(a.splitlines()):
    for i,x in enumerate(y):
        if x == "#": 
            if i not in dic: dic[i] = {}
            dic[i][j] = [0]
            #active.append([i,j,0])
for x in dic:
    for y in dic[x]:
        print(x,y,dic[x][y])

numNeighbs([1,1,1])

#for x in active: print(x)