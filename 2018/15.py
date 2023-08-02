a="""################################
##############.#################
##########G##....###############
#########.....G.################
#########...........############
#########...........############
##########.....G...#############
###########.........############
########.#.#..#..G....##########
#######..........G......########
##..GG..................###.####
##G..........................###
####G.G.....G.#####...E.#.G..###
#....##......#######........####
#.GG.#####.G#########.......####
###..####...#########..E...#####
#...####....#########........###
#.G.###.....#########....E....##
#..####...G.#########E.....E..##
#..###G......#######E.........##
#..##.........#####..........###
#......................#..E....#
##...G........G.......#...E...##
##............#..........#..####
###.....#...#.##..#......#######
#####.###...#######...#..#######
#########...E######....#########
###########...######.###########
############..#####..###########
#############.E..##.############
################.#..############
################################"""
test="""#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########"""
a=test
b=[[x for x in y] for y in a.splitlines()]
units = []
dirDeltas = [(0,-1),(1,0),(0,1),(-1,0)]

def walkDirect(c1,c2):
    x,y=c1
    candidates = [(x+dx, y+dy) for dx,dy in dirDeltas]
    return min(candidates,key=lambda x,y: (x,y,manhattan((x,y),c2)))


def canWalkDirect(c1,c2):
    while c1!=c2:
        x,y = c1
        if b[y][x] != ".": return False
        c1 = walkDirect(c1,c2)
    return True


def manhattan(a,b):
    x,y=a
    xx,yy=b
    return abs(xx-x)+abs(yy-y)


class Unit:
    def __init__(self, position, isElf):
        self.x = position[0]
        self.y = position[1]
        self.isElf = isElf
        self.hitPoints = 200
        self.attackPower = 3
        self.isAlive = True

    def target(self):
        rangeSquares = set()
        for candidate in [x for x in units if x.isElf  != self.isElf]:
            for dx,dy in dirDeltas: 
                x,y = candidate.x+dx, candidate.y+dy
                if b[y][x] == ".":
                    rangeSquares.add((x,y))
        rangeSquares = sorted(list(rangeSquares))
        for x in rangeSquares:
            print(canWalkDirect(x))
        #print(rangeSquares)

    def move(self, position):
        x,y = position
        b[self.y][self.x] = "."
        b[y][x] = "E" if self.isElf else "G"
        self.x,self.y = x,y

        # print(self.isElf, self.x, self.y, rangeSquares)
        # for j,y in enumerate(b):
        #     print("".join(["?" if (i,j) in rangeSquares else x for i,x in enumerate(y)]))



[[units.append(Unit(position=(i,j), isElf=(x=="E"))) for i,x in enumerate(y) if x in "GE"] for j,y in enumerate(b)]

for unit in units: 
    #print(unit.x,unit.y,unit.isElf,unit.hitPoints,unit.attackPower)
    unit.target()