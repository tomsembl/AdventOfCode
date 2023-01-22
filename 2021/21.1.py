p1,p2=[8,5]
p1,p2=[4,8]
s1,s2=[0,0]
p1-=1
p2-=1
rolls,boardCap,diceCap,goal=3,10,100,1000
count=None
for i in range(1,1000000000,6):
    p1=(p1+(i%diceCap)*rolls+3)%boardCap
    s1+=p1+1
    if s1>=goal: 
        count=i+2
        break
    p2=(p2+((i+3)%diceCap)*3+3)%10
    s2+=p2+1
    if s2>=goal: 
        count=i+5
        break
print(min(s1,s2)*count)#part1

#part 2
p1,p2=[8,5]
p1,p2=[4,8]
p1-=1
p2-=1
dic={}#gets the 3 rolls collapsed into one number and the number of universes
for x in range(1,4):
    for y in range(1,4):
        for z in range(1,4):
            if x+y+z not in dic: dic[x+y+z]=0
            dic[x+y+z]+=1
for x in dic:
    print(x,dic[x])
#[p1,p2],[s1,s2],universes,who
queue=[[[p1,p2],[0,0],[1,1]]]
goal=21
universeCounts=[0,0]
iterations=0
while queue:
    iterations += 1
    if iterations%100000==0: print(iterations,universeCounts)
    players, scores, universes = queue.pop()
    #player, score, u = players[who], scores[who], universes[who]
    for roll,freq in dic.items():
        for roll2,freq2 in dic.items():
            newPlayers, newScores, newUniverses = players[:], scores[:], universes[:]
            newPlayers[0] = (players[0]+roll)%boardCap
            newScores[0] = scores[0]+newPlayers[0]+1
            newUniverses[0] = universes[0]*freq
            if newScores[0] >= goal: 
                universeCounts[0] += newUniverses[0]
                continue
            newPlayers[1] = (players[1]+roll2)%boardCap
            newScores[1] = scores[1]+newPlayers[1]+1
            newUniverses[1] = universes[1]*freq2
            if newScores[1] >= goal: 
                universeCounts[1] += newUniverses[1]
                continue
            queue.append([newPlayers, newScores, newUniverses])
print(universeCounts)




