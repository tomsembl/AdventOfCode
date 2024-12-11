a="""0 4 4979 24 4356119 914 85734 698829"""
test="""125 17"""
#a=test
b=[int(x) for x in a.split()]

def do():
    global b
    newB = []
    for x in b:
        if x == 0:
            newB.append(1)
        elif len(str(x)) % 2 == 0:
            half1 = int(str(x)[:len(str(x))//2])
            half2 = int(str(x)[len(str(x))//2:])
            #print(x, half1, half2)
            newB.append(half1)
            newB.append(half2)
        else:
            newB.append(x*2024)
    #print(newB)
    b = newB
for i in range(25):
    #print(i)
    do()
#print(b)
print(len(b)) #p1

b=[int(x) for x in a.split()]
from functools import cache

@cache
def recurse(rock, blinks):
    if blinks == 0: 
        return 1
    if rock == 0: 
        return recurse(1, blinks - 1)
    s = str(rock)
    if len(s) % 2 == 0: 
        return recurse(int(s[:len(s) // 2]), blinks - 1) + recurse(int(s[len(s) // 2:]), blinks - 1)
    return recurse(rock * 2024, blinks - 1)

print(sum(recurse(x, 75) for x in b))