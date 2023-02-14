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
test="""Player 1:
43
19

Player 2:
2
29
14"""
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
    

GlobalGameCounter=0
b=[[int(y) for y in x.splitlines()[1:]] for x in a.split("\n\n")]
def playGame(b):
    cache={}
  

    global GlobalGameCounter
    gamecounter=0
    if not bool(GlobalGameCounter%10000): print(GlobalGameCounter)
    while True:
        gamecounter+=1
        GlobalGameCounter+=1
        if tuple(b[0]) in cache:
            if tuple(b[1]) in cache[tuple(b[0])]:
        #if gamecounter>1_000:
                #print(">1000")
                return 0,b
        else: 
            cache[tuple(b[0])]=set({})
        cache[tuple(b[0])].add(tuple(b[1]))
        if len(b[0])==0 or len(b[1])==0:
            return int(len(b[0])==0),b
        c1,c2=[b[0].pop(0),b[1].pop(0)]
        if c1<=len(b[0]) and c2<=len(b[0]):
            winner,_ = playGame([b[0][::][:c1],b[1][::][:c2]])
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

