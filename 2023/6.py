
def part(times,distances):
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
#part 1 input
times=[49,78,79,80]
distances=[298,1185,1066,1181]
part(times,distances)

#part 2 input
times=[49787980]
distances=[298118510661181]
part(times,distances)