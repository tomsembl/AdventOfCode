a=[1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,67,71,73,79,83,89,97,101,103,107,109,113]
test=[1,2,3,4,5,7,8,9,10,11]
#a=test
target = 0

def product(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def getGroup(availableNums):
    count = 0
    queue = [[x] for x in availableNums[::-1]]
    seen = set()
    validGroups = set()
    while queue:
        group = queue.pop(0)
        groupSum = sum(group)
        for y in [x for x in availableNums if x not in group]:
            if groupSum + y > target: continue
            new = group + [y]
            newTuple = tuple(sorted(new))
            if groupSum + y == target: 
                validGroups.add(newTuple)
                count += 1
                if count % 10 == 0: 
                    return product(sorted(list(validGroups),key= lambda x: product(x))[0])
                continue
            if newTuple not in seen:
                seen.add(newTuple)
                queue.append(new)

def part(p):
    global target
    target = sum(a) // (2+p)
    print(getGroup(a))

part(1)
part(2)