a="""##.#.
#..#.
.....
....#
#.###"""
test="""....#
#..#.
#..##
..#..
#...."""
#a=test
b=[[".#".index(x) for x in y] for y in a.splitlines()]

w,h = len(b[0]),len(b)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
im = ax.imshow(b, vmax=1, vmin=0)#, cmap='sand')
cbar = ax.figure.colorbar(im, ax=ax)
def update_visualization(new_matrix):
    im.set_array(new_matrix)
    fig.canvas.draw()
    plt.pause(0.001)

def getAdj(x,y):
    return [b[y+dy][x+dx] for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]] if -1 < y+dy < h and -1 < x+dx < w]

def matrixToBin(matrix):
    return "".join(["".join([str(x) for x in y]) for y in matrix])

update_visualization(b)
seen=set()
#conway's game of life
while True:
    binB = matrixToBin(b)
    if binB in seen: break
    seen.add(binB)
    bCopy = [y[::] for y in b[::]]
    for j,y in enumerate(b):
        for i,x in enumerate(y):
            adj = getAdj(i,j)
            if x == 1: bCopy[j][i] = 1 if sum(adj) == 1 else 0
            if x == 0: bCopy[j][i] = 1 if sum(adj) in (1,2) else 0
    b = bCopy
    for y in b:
        print("".join([str(x) for x in y]))
    print()
    update_visualization(b)

print(int("0b"+matrixToBin(b)[::-1],2)) #part 1

plt.show()