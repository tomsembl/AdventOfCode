def check(x):
    x=str(x)
    last=x[0]
    double=False
    for i,y in enumerate(x):
        if y<last: return False
        if y==last and i!=0: double=True
        last=y
    return double
total=0
for x in range(108457,562041+1):
    if check(x):
        total+=1
print(total)#part1


def check(x):
    x=str(x)
    last=x[0]
    groups={}
    for i,y in enumerate(x):
        if y<last: return False
        if y not in groups: groups[y]=[]
        groups[y].append(i)
        last=y
    consecutive=False
    for val,poses in groups.items():
        if len(poses)==2 and abs(poses[0]-poses[1])==1: consecutive=True
    return consecutive

total=0
for x in range(108457,562041+1):
    if check(x):
        total+=1
print(total)
#1444 too low