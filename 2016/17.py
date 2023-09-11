a="pslxynzg"
test="ulqzkmiv"
#test="kglvqrro"
#test="ihgpwlah"
#test="hijkl"
#a=test
dirs = "UDLR"
dxdy = [(0,-1),(0,1),(-1,0),(1,0)]
size = 4
import hashlib

def hashIt(it): return hashlib.md5(it.encode('utf-8')).hexdigest()

def getOpenDoors(path):
    return [i for i,x in enumerate(hashIt(a+path)[:4]) if int(x,16)>10]

end=(3,3)
queue=[(0,0,"")]
min = 99
shortestPath = None
while queue:
    node = queue.pop(0)
    x,y,path = node
    lp = len(path)
    if lp >= min: continue
    if (x,y) == end:
        if lp < min:
            shortestPath = path
            min = lp
            print(min,shortestPath)
    for dir in getOpenDoors(path):
        dx,dy = dxdy[dir]
        xx,yy = x+dx,y+dy
        if 0<=xx<size and 0<=yy<size:
            queue.append((xx,yy,path+dirs[dir]))
print(shortestPath)
