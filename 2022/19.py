a="""Blueprint 1: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 2: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 12 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 4: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 12 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 6: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 7: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 15 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 11: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 12: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 13 obsidian.
Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 12 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 16: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 2 ore and 11 obsidian.
Blueprint 17: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 19: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 21: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 22: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 24: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 25: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 4 ore and 11 obsidian."""

test="""Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
a=test
blueprints = []

for line in a.splitlines():
    blueprint = {}
    blueprint["blueprint"] = int(line.split(":")[0].split()[1])
    for attrib in line.split(":")[1].split("."):
        if "ore robot" in attrib:
            blueprint[0] = [int(attrib.split("ore robot")[1].split()[1])]
        elif "clay robot" in attrib:
            blueprint[1] = [int(attrib.split("clay robot")[1].split()[1])]
        elif "obsidian robot" in attrib:
            blueprint[2] = [int(x) for x in attrib.split("obsidian robot")[1].strip().split() if x.isnumeric()]
        elif "geode robot" in attrib:
            blueprint[3] = [int(x) for x in attrib.split("geode robot")[1].strip().split() if x.isnumeric()]
            blueprint[3].insert(1, 0)
    blueprints.append(blueprint)

for blueprint in blueprints:
    print(blueprint)
print()

def reset():
    global minutesRemaining,rate,names,robots,robotsLastTurn,ores
    minutesRemaining = 24
    rate=1
    names = ["ore", "clay", "obsidian", "geode"]
    robots = [1,0,0,0]
    robotsLastTurn = [1,0,0,0]
    ores = [0,0,0,0]

reset()
count = 0
candidates = []
for blueprint in blueprints:
    
    print()
    print(blueprint)
    for n in range(2**(minutesRemaining-2),(2**minutesRemaining)+1):
        if not n%1000000:print(bin(n),count)
        while minutesRemaining > 0:
            if 1<<minutesRemaining & n:
                if blueprint[0][0] <= ores[0]:
                    ores[0] -= blueprint[0][0]
                    robots[0] += 1
                else:break
                for i in range(4):
                    ores[i] += robots[i]
            minutesRemaining -= 1
        count += 1
        candidates.append(bin(n))
            # print("minutes",minutesRemaining,"ores", ores,"robots", robots)
            # minutesRemaining -= 1
            # for i in range(4):
            #     ores[i] += robots[i] * rate
            # robots = robotsLastTurn
            # for j in range(3,-1,-1):
            #     if all([ores[i] >= oreCost for i,oreCost in enumerate(blueprint[j])]):
            #         for i,oreCost in enumerate(blueprint[i]):
            #             ores[i] -= oreCost
            #             robotsLastTurn[i] += 1
    print(ores)
