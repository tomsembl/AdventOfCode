a="""Player 1:
47
19
22
31
24
6
10
5
1
48
46
27
8
45
16
28
33
41
42
36
50
39
30
11
17

Player 2:
4
18
21
37
34
15
35
38
20
23
9
25
32
13
26
2
12
44
14
49
3
40
7
43
29"""
test="""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
#a=test
# b=[[int(y) for y in x.splitlines()[1:]] for x in a.split("\n\n")]
# while len(b[0])!=0 and len(b[1])!=0:
#     c1,c2=[b[0].pop(0),b[1].pop(0)]
#     winner = int(c1<c2)
#     b[winner]+=[c2,c1] if winner else [c1,c2]
# # print(b)
# total=0
# lenb=len(b[winner])
# for x in range(lenb):
#     total += (lenb-x)*b[winner][x]
# print(total)#part1
    

gameCounter=0
b=[[int(y) for y in x.splitlines()[1:]] for x in a.split("\n\n")]
def playGame(b):
    cache={}
    def writeCache(key): 
        parent=cache
        for player in key:
            for node in player:
                if node not in parent: parent[node] = {}
                parent=parent[node]
            parent[-1]={}
            parent=parent[-1]
    def readCache(key): 
        parent=cache
        for player in key:
            for node in player:
                if node not in parent: return False
                parent=parent[node]
            if -1 not in parent: return False
            parent=parent[-1]
        return True

    global gameCounter
    gameCounter+=1
    if not bool(gameCounter%1): print(gameCounter)
    while True:
        if readCache(b):
            return 0,b
        else: 
            writeCache(b)
        if len(b[0])==0 or len(b[1])==0:
            return int(len(b[0])==0),b
        c1,c2=[b[0].pop(0),b[1].pop(0)]
        if c1<=len(b[0]) and c2<=len(b[0]):
            winner,b2 = playGame([b[0][:c1],b[1][:c2]])
        else: winner = int(c1<c2)
        b[winner]+=[c2,c1] if winner else [c1,c2]

winner,b2 = playGame(b)
print(winner,b2)
total=0
lenb=len(b[winner])
for x in range(lenb):
    total += (lenb-x)*b[winner][x]
print(total)#part2

#33455 too high

