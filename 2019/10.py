a="""....#.....#.#...##..........#.......#......
.....#...####..##...#......#.........#.....
.#.#...#..........#.....#.##.......#...#..#
.#..#...........#..#..#.#.......####.....#.
##..#.................#...#..........##.##.
#..##.#...#.....##.#..#...#..#..#....#....#
##...#.............#.#..........#...#.....#
#.#..##.#.#..#.#...#.....#.#.............#.
...#..##....#........#.....................
##....###..#.#.......#...#..........#..#..#
....#.#....##...###......#......#...#......
.........#.#.....#..#........#..#..##..#...
....##...#..##...#.....##.#..#....#........
............#....######......##......#...#.
#...........##...#.#......#....#....#......
......#.....#.#....#...##.###.....#...#.#..
..#.....##..........#..........#...........
..#.#..#......#......#.....#...##.......##.
.#..#....##......#.............#...........
..##.#.....#.........#....###.........#..#.
...#....#...#.#.......#...#.#.....#........
...####........#...#....#....#........##..#
.#...........#.................#...#...#..#
#................#......#..#...........#..#
..#.#.......#...........#.#......#.........
....#............#.............#.####.#.#..
.....##....#..#...........###........#...#.
.#.....#...#.#...#..#..........#..#.#......
.#.##...#........#..#...##...#...#...#.#.#.
#.......#...#...###..#....#..#...#.........
.....#...##...#.###.#...##..........##.###.
..#.....#.##..#.....#..#.....#....#....#..#
.....#.....#..............####.#.........#.
..#..#.#..#.....#..........#..#....#....#..
#.....#.#......##.....#...#...#.......#.#..
..##.##...........#..........#.............
...#..##....#...##..##......#........#....#
.....#..........##.#.##..#....##..#........
.#...#...#......#..#.##.....#...#.....##...
...##.#....#...........####.#....#.#....#..
...#....#.#..#.........#.......#..#...##...
...##..............#......#................
........................#....##..#........#"""
test="""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
#a=test
b=a.splitlines()

def lcd(i,j):
    minimum = min([abs(i),abs(j)])
    if 0 in [i,j]: minimum = max([abs(i),abs(j)])
    div=1
    for x in range(minimum+1,1,-1):
        if i%x==0 and j%x==0: 
            div=x
            break
    return div

dic={}
for j,y in enumerate(b):
    for i,x in enumerate(y):
        if x=="#":
            dic[(i,j)]=[]
            for j2,y2 in enumerate(b):
                for i2,x2 in enumerate(y2):
                    if i2 == i and j2 == j:continue #skip main asteroid
                    if x2 == "#":
                        xDiff, yDiff = i2-i, j2-j
                        lcd_ = lcd(xDiff,yDiff)
                        xLCD,yLCD = xDiff//lcd_, yDiff//lcd_
                        #print(xDiff,yDiff,xLCD,yLCD)
                        multiple = 1
                        #maxMultiple = xLCD//multiple
                        inShadow = False
                        while multiple < lcd_:
                            if b[j+yLCD*multiple][i+xLCD*multiple] == "#": 
                                inShadow = True
                                break
                            multiple += 1
                        if not inShadow:
                            dic[(i,j)].append((i2,j2))

for x in dic:
    print(x,len(dic[x]))
print(len(sorted(dic.values(),key=lambda x: len(x))[-1]))
                        


