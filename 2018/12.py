a="""#....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##"""

b=""".#.## => #
.#.#. => #
#.#.# => .
.#### => .
.#... => .
#..## => .
..#.# => #
#.#.. => .
##### => .
....# => .
...## => .
..##. => .
##.#. => #
##..# => .
##... => #
..### => #
.##.. => #
###.. => .
#..#. => .
##.## => .
..#.. => #
.##.# => #
####. => #
#.### => .
#...# => #
###.# => #
...#. => #
.###. => .
.#..# => #
..... => .
#.... => .
#.##. => #"""

# a="""...#..#.#..##......###...###..........."""

# b="""...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #"""
def toBin(string): return string.replace("#","1").replace(".","0")
def toInt(string): return int("0b"+string,2)
def trim2(string): 
    while string[0] == "0": string = string[1:]
    while string[-1] == "0": string = string[:-1]
    return string


iterations = 50000000000#20
offset = None
def doTheThing(iterations):
    c = [toInt(toBin(y[0])) for y in [x.split(" => ") for x in b.splitlines()] if y[1]=="#"]
    d = toBin(a)
    buffer = 8
    buf = "0"*buffer
    global offset
    offset = a.index("#")
    last = trim2(d)
    for j in range(iterations):
        if d[:buffer] != buf: 
            d = buf + d
            offset += buffer
        if d[-buffer:] != buf:  d += buf
        new = "00"
        for i in range(2,len(d)-2): 
            new += str(int(toInt(d[i-2:i+3]) in c))
        new += "00"
        d = new
        print(d)
        newLast = trim2(d)
        if newLast == last: 
            offset -= iterations - j - 1
            break
        last = newLast
    return d

d = doTheThing(20)
print(sum([i-offset for i,x in enumerate(d) if x=="1"])) #part 1

d = doTheThing(50000000000)
print(sum([i-offset for i,x in enumerate(d) if x=="1"])) #part 2
#750000000712 too high