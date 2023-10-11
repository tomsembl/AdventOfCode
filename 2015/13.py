a="""Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George."""

test="""Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
#a=test
hap={}
for x in [y.split() for y in a.splitlines()]:
    p1, h, p2 = x[0], int({"lose":"-","gain":"+"}[x[2]]+x[3]), x[-1][:-1]
    if p1 not in hap: hap[p1]={}
    hap[p1][p2]=h
lHap = len(hap)

def scoreTable(table):
    global hap
    total = 0
    for i,x in enumerate(table):
        total += hap[x][table[i-1]]
        total += hap[x][table[(i+1)%lHap]]
    return total

queue=[[x] for x in hap]
happiestTable = 0
while queue:
    table = queue.pop()
    if len(table) == lHap:
        score = scoreTable(table)
        if score > happiestTable:
            happiestTable = score
    for next in [x for x in hap if x not in table]:
        queue.append(table+[next])
print(happiestTable) #part 1


hap={}
for x in [y.split() for y in a.splitlines()]:
    p1, h, p2 = x[0], int({"lose":"-","gain":"+"}[x[2]]+x[3]), x[-1][:-1]
    if p1 not in hap: hap[p1]={}
    hap[p1][p2]=h
for x in hap:
    hap[x]["me"] = 0
hap["me"]={x:0 for x in hap}
lHap = len(hap)

def scoreTable(table):
    global hap
    total = 0
    for i,x in enumerate(table):
        total += hap[x][table[i-1]]
        total += hap[x][table[(i+1)%lHap]]
    return total

queue=[[x] for x in hap]
happiestTable = 0
while queue:
    table = queue.pop()
    if len(table) == lHap:
        score = scoreTable(table)
        if score > happiestTable:
            happiestTable = score
    for next in [x for x in hap if x not in table]:
        queue.append(table+[next])
print(happiestTable) #part 2