a=1362
end=(31,39)

# test=10
# a=test
# end=(7,4)

size = 100
def getWalls(x,y):
    return int( bin(x*x + 3*x + 2*x*y + y + y*y + a).count("1") % 2 != 0)
matrix = [[getWalls(x,y) for x in range(size)] for y in range(size)]
matrixCopy= matrix[::]
# for y in matrix:
#     print("".join([".#"[x] for x in y]))
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
im = ax.imshow(matrix, vmax=2, vmin=0)#, cmap='sand')
cbar = ax.figure.colorbar(im, ax=ax)
def update_visualization(new_matrix):
    im.set_array(new_matrix)
    fig.canvas.draw()
    plt.pause(0.001)



dirs=[(0,1),(1,0),(0,-1),(-1,0)]
queue=[(1,1,0)]
seen={}
while queue:
    node = queue.pop(0)
    x,y,dist = node
    if (x,y) not in seen:
        seen[(x,y)] = dist
    elif dist >= seen[(x,y)]:
        continue
    # matrixCopy[y][x] = 2
    # update_visualization(matrixCopy)
    if (x,y) == end:
        print(dist)
        break
    for dx,dy in dirs:
        xx,yy=x+dx,y+dy
        if 0 <= xx < size and 0 <= yy < size:
            if matrix[yy][xx] == 0:
                queue.append((xx,yy,dist+1))

matrixCopy= matrix[::]
queue=[(1,1,0)]
seen={}
while queue:
    node = queue.pop(0)
    x,y,dist = node
    if (x,y) not in seen:
        seen[(x,y)] = dist
    elif dist >= seen[(x,y)]:
        continue
    if dist >= 50: continue
    # matrixCopy[y][x] = 2+dist
    # update_visualization(matrixCopy)
    for dx,dy in dirs:
        xx,yy = x+dx,y+dy
        if 0 <= xx < size and 0 <= yy < size:
            if matrix[yy][xx] == 0:
                queue.append((xx,yy,dist+1))
print(len(seen))
#139 too high

#plt.show()