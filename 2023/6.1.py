a="""Time:        49     78     79     80
Distance:   298   1185   1066   1181"""
test="""Time:      7  15   30
Distance:  9  40  200"""
times=[49787980]
distances=[298118510661181]

#test
# times=[7,15,30]
# distances=[9,40,200]

total = 1
for i,t in enumerate(times):
    raceTotal = 0
    distance = distances[i]
    for s in range(t):
        moveTime = t - s
        if moveTime * s > distance:
           raceTotal += 1 
    total *= raceTotal
print(total)