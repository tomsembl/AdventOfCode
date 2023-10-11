a="""Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."""
test="""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
#a=test
flying,resting,distances,speeds,durations,rests,scores = {},{},{},{},{},{},{}
for x in[y.split() for y in a.splitlines()]:
    reindeer,speed,duration,rest = x[0],int(x[3]),int(x[6]),int(x[-2])
    flying[reindeer] = duration
    speeds[reindeer] = speed
    durations[reindeer] = duration
    rests[reindeer] = rest
    distances[reindeer] = 0
    scores[reindeer] = 0

for t in range(2503):
    for f in list(flying):
        flying[f] -= 1
        if flying[f] == 0:
            resting[f] = rests[f] + 1
            del flying[f]
        distances[f] += speeds[f]
    for r in resting:
        resting[r] -= 1
        if resting[r] == 0:
            flying[r] = durations[r]
    for d in distances:
        top=max(distances.values())
        if distances[d] == top:
            scores[d] += 1
print(distances[max(distances,key=lambda x: distances[x])])
print(scores[max(scores,key=lambda x: scores[x])])