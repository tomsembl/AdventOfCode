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
test="""#########0
#G..G..G#1
#.......#2
#.......#3
#G..E..G#4
#.......#5
#.......#6
#G..G..G#7
#########8
012345678"""
test="""#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#   
####### """
test="""#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""
test="""#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""
#a=test

dirDeltas = [(0,-1),(1,0),(0,1),(-1,0)]

def dijkstraSelectTarget(a,candidates):
    queue = [(a,0)]
    parents = {a:(set({}),0)}
    seen = set()
    targetFound = False
    maxDistance = None
    targets = []
    target = None
    while queue:
        c,distance = queue.pop(0)
        if targetFound:
            if distance > maxDistance: 
                target = min(targets,key=lambda x:(x[1],x[0]))
                break
        if c in candidates: 
            targetFound = True
            maxDistance = distance
            targets.append(c)
            target=c
            continue
        for next in getOpenSquares(c):
            if next in parents:
                if parents[next][1] != distance+1: continue
                parents[next][0].add(c)
            else: parents[next] = [set({c}),distance+1]
            if next in seen: continue
            queue.append((next,distance+1))
            seen.add(next)

    if not target: return False
    queue = [target]
    seen = set()
    ones = set()
    while True:
        node = queue.pop(0)
        parentSet, distance = parents[node]
        if distance == 1: ones.add(node)
        if parentSet == set({}):
            return min(ones,key=lambda x:(x[1],x[0]))
        for next in parentSet:
            if next in seen: continue
            queue.append(next)
            seen.add(next)

def manhattan(a,b):
    x,y=a
    xx,yy=b
    return abs(xx-x)+abs(yy-y)

def getOpenSquares(c):
    return [(x,y) for x,y in [(c[0]+dx, c[1]+dy) for dx,dy in dirDeltas] if grid[y][x] == "."]

class Unit:
    def __init__(self, position, isElf):
        self.x, self.y = position
        self.isElf = isElf
        self.hitPoints = 200
        self.attackPower = elvesAttackPower if isElf else 3
        self.isAlive = True

    def getTarget(self):
        enemyOpenSquares = set()
        enemies = self.getEnemies()
        for candidateEnemy in enemies:
            for openSquare in getOpenSquares((candidateEnemy.x,candidateEnemy.y)):
                enemyOpenSquares.add(openSquare)
        enemyOpenSquares = sorted(list(enemyOpenSquares))
        target = dijkstraSelectTarget((self.x,self.y),enemyOpenSquares)
        return target

    def move(self, position):
        x,y = position
        grid[self.y][self.x] = "."
        grid[y][x] = "E" if self.isElf else "G"
        self.x,self.y = x,y

    def getEnemies(self): return [x for x in units if x.isElf != self.isElf and x.isAlive]

    def getAdjacentEnemies(self):
        adjacentCoords = [(self.x+dx, self.y+dy) for dx,dy in dirDeltas]
        return [e for e in self.getEnemies() if (e.x,e.y) in [(x,y) for x,y in adjacentCoords]]

    def attack(self,enemy):
        enemy.hitPoints -= self.attackPower
        if enemy.hitPoints <= 0: enemy.die()

    def die(self): 
        self.isAlive = False
        grid[self.y][self.x] = "."

for elvesAttackPower in range(3,100):
    grid=[[x for x in y] for y in a.splitlines()]
    round = 1
    units = []
    [[units.append(Unit(position=(i,j), isElf=(x=="E"))) for i,x in enumerate(y) if x in "GE"] for j,y in enumerate(grid)]
    elvesBefore = len([unit for unit in units if unit.isElf])
    units.sort(key=lambda x:(x.y,x.x))
    endFlag=False
    while True:
        # for y in grid:
        #     print(" ".join(y))
        # #print(", ".join([f"{'GE'[int(x.isElf)]}({x.hitPoints})" for x in units]))
        # print(f"\nAfter {round} rounds:")
        for unit in units: 
            if not unit.isAlive: continue
            if not unit.getEnemies():
                endFlag=True
                break
            if not unit.getAdjacentEnemies():
                target = unit.getTarget()
                if target:
                    unit.move(target)
            adjacentEnemies = unit.getAdjacentEnemies()
            if adjacentEnemies:
                enemy = min(adjacentEnemies,key=lambda x:(x.hitPoints,x.y,x.x))
                unit.attack(enemy)
                continue
        if endFlag: 
            outcome = sum([x.hitPoints for x in units if x.isAlive])
            outcome*= (round-1)
            #print(outcome) #part 1
            break
        round += 1
        units.sort(key=lambda x:(x.y,x.x))
    elvesAfter = len([unit for unit in units if unit.isElf and unit.isAlive])
    if elvesBefore==elvesAfter:
        outcome = sum([x.hitPoints for x in units if x.isAlive])
        outcome*= (round-1)
        print(outcome) #part 2 #50724 too low
        break