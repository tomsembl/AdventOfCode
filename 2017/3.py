#a=347991
# for a in range(1,32):
#     x=0
#     while x**2 < a:
#         x+=1
#     xSq1,xSq2=(x-1)**2,x**2
#     sqDiff=xSq2-xSq1
#     isEven=(x-1)%2==0
#     dist1 = x // 2
#     dist2 = a - xSq1 - (sqDiff+2) // 2
#     print(a,dist1,dist2)
a=347991
dirs=[[1,0],[0,-1],[-1,0],[0,1]]
dir = 0
x,y = 0,0
n=2
total=1
while total < a:
    mul = n//2
    total += mul
    if total > a:
        mul -= total-a
    x,y = x+dirs[dir][0]*mul,y+dirs[dir][1]*mul
    dir+=1
    dir%=4
    n+=1

def manhattan(x,y,xx,yy):
    return abs(x-xx) + abs(y-yy)

print(manhattan(x,y,0,0)) #part 1: 480

def doTheThing():
    current = 1
    dir = 0
    x,y = 0,0
    n=2
    total=1
    dict_={}
    dirs2 = dirs+ [[1,1],[-1,-1],[-1,1],[1,-1]]

    def getNeighSum(c):
        x,y = c
        return sum([dict_[(x+xx,y+yy)] for xx,yy in dirs2 if (x+xx,y+yy) in dict_])


    while True:
        mul = n//2
        total += mul
        if total > a:
            mul -= total-a
        for _ in range(mul):
            dict_[(x,y)] = current
            x,y = x+dirs[dir][0],y+dirs[dir][1]
            current = getNeighSum((x,y))
            if current > a: 
                return current
                
        dir+=1
        dir%=4
        n+=1
print(doTheThing())#part 2: 349975