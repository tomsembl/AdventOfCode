a="""11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"""
test="""0 2 7 0"""
#a=test
b = [int(x) for x in a.split()]
leng = len(b)
seen = set()
nCycles = 0
while tuple(b) not in seen:
    seen.add(tuple(b))
    nCycles += 1
    i,x = min([(i,x) for i,x in enumerate(b)],key=lambda x: (-x[1],x[0]))
    b[i] = 0
    for y in range(1,x+1):
        b[(i+y)%leng] += 1
print(nCycles)#part 1: 4074