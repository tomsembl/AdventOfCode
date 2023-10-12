a="""33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42"""
test="""20
15
10
5
5"""
#a=test
target=25
target=150
b=[int(x) for x in a.splitlines()]
lenB=len(b)
queue=[(x,) for x in range(lenB)]
seen={y:sum([b[x] for x in y]) for y in queue}
while queue:
    node = queue.pop()
    if seen[node] >= target: continue
    for next in [x for x in range(lenB) if x not in node]:
        nextNode = node+(next,)
        nextNode = tuple(sorted(list(nextNode)))
        if nextNode in seen: continue
        seen[nextNode] = sum([b[x] for x in nextNode])
        queue.append(nextNode)
print(len([x for x in seen.values() if x==target])) #part 1
minLen = min([len(x) for x in seen if seen[x] == target])
print(len([x for x in seen if seen[x] == target and len(x) == minLen])) #part 2
