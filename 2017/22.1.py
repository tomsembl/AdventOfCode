a="""##########..#.###...##..#
##....#...#....#..####.#.
#..#.##..#..##.###..#.###
.#.#.......####.....#.#..
...######....#.##########
##.#.....#.#####.#....###
#.####.#..#.#.#...#.#..##
#.##..#####..###..###.##.
#.####.#.##.##...#.#.#.##
#.#.#......##.##..###.#.#
#...#.#..#.##....#.##..##
.#.....##.##..#.####..##.
.#......#.#.########..###
##....###.#.#.###...##..#
..##.###....#.....#...#.#
....##...##...##.##.#..##
..#.#.#..#######..###..##
......#####.#####..#.#..#
.####.#......#..###..#.##
#....####.#..#.##.###.##.
####.#...##....###...#.#.
#####.#......#.#..###.##.
#.##.#..#..#..#.....#.#.#
#...#.#.##.#.####.#.#..#.
.##.##..#..###.##.....###"""
test="""..#
#..
..."""
#a=test
b=[['.#'.index(x) for x in y] for y in a.splitlines()]
infected,weakened,flagged,clean = set(),set(),set(),set()
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
dir = 0
size = len(b)
mid = size//2
x,y = mid,mid

for j in range(size):
    for i in range(size):
        if b[j][i]==1: infected.add((i,j))

total = 0
for burst in range(10_000_000):
    if (x,y) in infected:
        dir += 1
        infected.remove((x,y))
        flagged.add((x,y))
    elif (x,y) in weakened:
        weakened.remove((x,y))
        infected.add((x,y))
        total += 1
    elif (x,y) in flagged:
        dir += 2
        flagged.remove((x,y))
    else:
        weakened.add((x,y))
        dir += -1
    dir %= 4
    dx,dy = dirs[dir]
    x,y = x+dx,y+dy
print(total)
#5431 too high