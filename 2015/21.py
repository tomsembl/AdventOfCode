weapons = [ 
    {"cost":8,   "dmg":4,  "arm":0},
    {"cost":10,  "dmg":5,  "arm":0},
    {"cost":25,  "dmg":6,  "arm":0},
    {"cost":40,  "dmg":7,  "arm":0},
    {"cost":74,  "dmg":8,  "arm":0},
]
armours = [
    {"cost":0,   "dmg":0,  "arm":0},
    {"cost":13,  "dmg":0,  "arm":1},
    {"cost":31,  "dmg":0,  "arm":2},
    {"cost":53,  "dmg":0,  "arm":3},
    {"cost":75,  "dmg":0,  "arm":4},
    {"cost":102, "dmg":0,  "arm":5},
]
rings = [
    {"cost":25,  "dmg":1,  "arm":0},
    {"cost":50,  "dmg":2,  "arm":0},
    {"cost":100, "dmg":3,  "arm":0},
    {"cost":20,  "dmg":0,  "arm":1},
    {"cost":40,  "dmg":0,  "arm":2},
    {"cost":80, "dmg":0,  "arm":3},
]

boss = {"hp":100,"dmg":8,"arm":2}
player = {"hp":100,"dmg":0,"arm":0}
# boss = {"hp":12,"dmg":7,"arm":2}
# player = {"hp":8,"dmg":5,"arm":5}

def fight(players):
    i=0
    while True:
        netDmg = players[i]["dmg"] - players[1-i]["arm"]
        if netDmg < 1: netDmg = 1
        players[1-i]["hp"] -= netDmg
        if players[1-i]["hp"] < 1:
            return i
        i=1-i

ringPerms = [[]]
for x in rings: ringPerms.append([x])
for j,y in enumerate(rings): 
    for i,x in enumerate(rings): 
        if i!=j: ringPerms.append([x,y])

builds=set()
for weapon in weapons:
    for armour in armours:
        for ringPerm in ringPerms:
            cost = weapon["cost"] + armour["cost"] + sum([x["cost"] for x in ringPerm])
            dmg = weapon["dmg"] + armour["dmg"] + sum([x["dmg"] for x in ringPerm])
            arm = weapon["arm"] + armour["arm"] + sum([x["arm"] for x in ringPerm])
            builds.add((cost,dmg,arm))
minCostWin = 9999
for build in builds:
    cost,dmg,arm = build
    result = fight([{"hp":player["hp"],"dmg":dmg,"arm":arm},{"hp":boss["hp"],"dmg":boss["dmg"],"arm":boss["arm"]}])
    if result == 0:
        if cost < minCostWin:
            minCostWin = cost
print(minCostWin)

maxCostloss = 0
for build in builds:
    cost,dmg,arm = build
    result = fight([{"hp":player["hp"],"dmg":dmg,"arm":arm},{"hp":boss["hp"],"dmg":boss["dmg"],"arm":boss["arm"]}])
    if result == 1:
        if cost > maxCostloss:
            maxCostloss = cost
print(maxCostloss)
