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

b = [int(x) for x in a.split()]
leng = len(b)
seen = {}
nCycles = 0
iterations = 0
while iterations < 1_000_000:
    if iterations%100_000 == 0: print(iterations)
    iterations += 1
    c = tuple(b)
    if c not in seen:
        seen[c] = 0
    seen[c] += 1 
    nCycles += 1
    i,x = min([(i,x) for i,x in enumerate(b)],key=lambda x: (-x[1],x[0]))
    b[i] = 0
    for y in range(1,x+1):
        b[(i+y)%leng] += 1
print(sum([1 if seen[x]>1 else 0 for x in seen]))#part 2: