a="""Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

test="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
#a=test
lst=[]
for x in [y.split() for y in a.splitlines()]:
    x,y,z,zz,zzz = int(x[2][:-1]), int(x[4][:-1]), int(x[6][:-1]), int(x[8][:-1]), int(x[10])
    lst.append([x,y,z,zz,zzz])
best=0
for x in range(101):
    for y in range(101-x):
        for z in range(101-x-y):
            for zz in range(101-x-y-z):
                if x+y+z+zz == 100:
                    lst2 = [x,y,z,zz]
                    capacity = sum([lst2[i]*lst[i][0] for i in range(4)])
                    durability = sum([lst2[i]*lst[i][1] for i in range(4)])
                    flavor = sum([lst2[i]*lst[i][2] for i in range(4)])
                    texture = sum([lst2[i]*lst[i][3] for i in range(4)])
                    if any([capacity<=0,durability<=0,flavor<=0,texture<=0]): continue
                    total = capacity * durability * flavor * texture
                    if total > best: 
                        best = total
print(best) #part 1

best=0
for x in range(101):
    for y in range(101-x):
        for z in range(101-x-y):
            for zz in range(101-x-y-z):
                if x+y+z+zz == 100:
                    lst2 = [x,y,z,zz]
                    calories = sum([lst2[i]*lst[i][4] for i in range(4)])
                    if calories != 500: 
                        continue
                    capacity = sum([lst2[i]*lst[i][0] for i in range(4)])
                    durability = sum([lst2[i]*lst[i][1] for i in range(4)])
                    flavor = sum([lst2[i]*lst[i][2] for i in range(4)])
                    texture = sum([lst2[i]*lst[i][3] for i in range(4)])
                    if any([capacity<=0,durability<=0,flavor<=0,texture<=0]): 
                        continue
                    total = capacity * durability * flavor * texture
                    if total > best: 
                        best = total
print(best) #part 2

                    