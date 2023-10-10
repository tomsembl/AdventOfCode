a="""Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70"""
test="""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
#a=test
dicti={}
for x in [y.split() for y in a.splitlines()]:
    source,dest,dist = x[0],x[2],int(x[4])
    if source not in dicti: dicti[source] = {}
    if dest not in dicti: dicti[dest] = {}
    dicti[source][dest] = dist
    dicti[dest][source] = dist
for x in dicti:
    print(x)
    print(dicti[x])
    print()
queue=[([x],0) for x in dicti]
shortestDist = 999999
longestDist = 0
lDict = len(dicti)
while queue:
    path,dist = queue.pop()
    current = path[-1]
    if len(path) == lDict:
        if dist < shortestDist:
            shortestDist = dist
        if dist > longestDist:
            longestDist = dist
    for next in [x for x in dicti[current] if x not in path]:
        queue.append((path+[next],dist+dicti[current][next]))
print(shortestDist)
print(longestDist)