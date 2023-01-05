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
import datetime
dateTime = str(datetime.datetime.now())[:19].replace(":", "-")
for line in a.splitlines():
    blueprint = []
    #blueprint["blueprint"] = int(line.split(":")[0].split()[1])
    for attrib in line.split(":")[1].split("."):
        if "ore robot" in attrib:
            blueprint.append([int(attrib.split("ore robot")[1].split()[1])])
        elif "clay robot" in attrib:
            blueprint.append([int(attrib.split("clay robot")[1].split()[1])])
        elif "obsidian robot" in attrib:
            blueprint.append([int(x) for x in attrib.split("obsidian robot")[1].strip().split() if x.isnumeric()])
        elif "geode robot" in attrib:
            blueprint.append([int(x) for x in attrib.split("geode robot")[1].strip().split() if x.isnumeric()])
            blueprint[3].insert(1, 0)
    blueprints.append(blueprint)

for blueprint in blueprints:
    print(blueprint)
print()

from datetime import datetime
geodesPerBP = []
def bfs(bpIndex,blueprint,duration=24):
    global queue,readQueue,readQueueMil,time
    pickleSize = 10000
    queue={0:(duration,[0,0,0,0],[1,0,0,0])}
    readQueue = queue
    readQueueMil = 0
    cache = {}
    times = [datetime.now()]
    durations = []
    maxProductionNeeded = [max([(blueprint[j]+[0,0])[i] for j in range(4)]) for i in range(3)]  #[[x[i] for x in y+[0,0]] for y in blueprint]
    print(maxProductionNeeded)

    def writeCache(key):
        node = cache
        for x in key:
            if x not in node:
                node[x] = {}
            node = node[x]

    def readCache(key):
        node = cache
        for x in key:
            if x not in node:
                return False
            node = node[x]
        return True
    
    import pickle
    def storeQueue():
        global queue
        if not queueCount % pickleSize:
            mil = queueCount // pickleSize
            with open(f'c:/temp/19/{dateTime}-{bpIndex}-{mil}.pkl', 'wb') as f:
                pickle.dump(queue, f) #pickling
            if iterations >= pickleSize:
                del queue
                queue = {}
                retreiveQueue(force=True)

    import os,sys
    def retreiveQueue(force=False):
        global readQueue,readQueueMil
        if queueCount-iterations < pickleSize:
            readQueue = queue
            return
        if iterations % pickleSize == 0:
            if iterations!=0: force = True
        if force:
            mil = ( iterations // pickleSize ) + 1
            if readQueueMil < mil:
                #print(f"unpickling #{mil} @{iterations}")
                picklePath = f'c:/temp/19/{dateTime}-{bpIndex}-{mil}.pkl'
                if not os.path.isfile(picklePath):
                    print("ERROR: file not found")
                with open(picklePath, 'rb') as f:
                    del readQueue
                    readQueue = pickle.load(f) #unpickling
                    readQueueMil = mil
                    #print("first:",list(readQueue.keys())[0],"last:",list(readQueue.keys())[-1])
                try: os.remove(f'c:/temp/19/{dateTime}-{bpIndex}-{mil-1}.pkl')#delete a file
                except: pass
        
    def getSize(d):
        size = sys.getsizeof(d)
        for key, value in d.items():
            if isinstance(value, dict):
                size += getSize(value)
            else:
                size += sys.getsizeof(value)
        return size

    maxGeodes = 0
    minTime = 24
    iterations = -1
    queueCount = 1
    while True:
        iterations += 1
        retreiveQueue()
        try:time, ores, bots = readQueue[iterations]
        except:
            print(f"break at {iterations}")
            break
        time, ores, bots = readQueue[iterations]
        if iterations % 100000 == 0:
            times.append(datetime.now())
            durations.append((times[-1]-times[-2]).total_seconds())
            minTime = min(minTime, time)
            for x in range(minTime+1,duration+1):
                try: del cache[minTime+1]
                except: pass
            print(bpIndex,iterations,queueCount,queueCount/(iterations if iterations else 1),minTime,time,ores,bots,"duration:",durations[-1],"avg:",str(sum(durations)/len(durations))[:4])#,f"{getSize(cache)//1_000_000}mb")
        key = (time,*ores,*bots)
        #if readCache(key): continue
        writeCache(key)
        if time == 0:
            if ores[3] > maxGeodes:
                maxGeodes = max(maxGeodes, ores[3])
                print(f"new max geodes:{maxGeodes}, ores:{ores}, bots:{bots}, blueprint:{blueprint},")
            continue
        for j in range(3,-1,-1):
            stop = False
            if j<3:
                if bots[j]*time + ores[j] >= maxProductionNeeded[j]*time:# or ores[j] >= maxProductionNeeded[j]*time: 
                    continue
            for i,oreCost in enumerate(blueprint[j]):#checking whether affordable given the current robots
                if bots[i] == 0: 
                    stop = True
                    break
            if stop: continue
            wait = 0
            for i,oreCost in enumerate(blueprint[j]):#checking whether affordable given the current ores, decrementing time if not.
                while ores[i]+(bots[i]*wait) < oreCost:
                    wait += 1
                    if time-1-wait < 0:
                        stop = True
                        break
                if stop: break  
            if stop: continue
            newOres = [ores[i]+x*(1+wait)-(blueprint[j]+[0,0,0])[i] for i,x in enumerate(bots)]
            newBots = [x+(1 if j==i else 0) for i,x in enumerate(bots)]
            storeQueue()
            newNode = [time-1-wait, newOres, newBots]
            key = (newNode[0],*newOres,*newBots)
            if readCache(key): continue
            queue[queueCount]=newNode
            queueCount+=1
        newOres = [ores[i]+x*(time) for i,x in enumerate(bots)]
        storeQueue()
        newNode = [0, newOres, bots]
        key = (newNode[0],*newOres,*newBots)
        if readCache(key): continue
        queue[queueCount] = newNode
        queueCount+=1
    print("final answer:",maxGeodes)
    readQueue,queue,cache=None,None,None
    geodesPerBP.append(maxGeodes)
    with open(f'c:/temp/19/{dateTime}-answer.txt', 'w') as f:
        f.write(str(geodesPerBP))
# for i,blueprint in enumerate(blueprints):
#     bfs(i,blueprint)
# print("geodesPerBP",geodesPerBP)
# print("answer:",sum([x*(i+1) for i,x in enumerate(geodesPerBP)])) #part1

#1009 win!

for i,blueprint in enumerate(blueprints[:3]):
    bfs(i,blueprint,duration=32)
print("geodesPerBP",geodesPerBP)
print("answer:",sum([x*(i+1) for i,x in enumerate(geodesPerBP)])) #part2