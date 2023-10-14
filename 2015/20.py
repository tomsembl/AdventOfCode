goal=34000000
# # goal=150
# a=[]
# for x in range(goal//10+1):
#     a.append(10)
# a[0]=0
# for y in range(2,goal//10+1):
#     for x in range(y,goal//10+1,y):
#         a[x] += y*10

# for i,x in enumerate(a):
#     if x >= goal:
#         print(i) #part 1
#         break



a=[]
for x in range(goal//10+1):
    a.append(0)
for y in range(1,goal//10+1):
    for x in range(y,50*y+1,y):
        if x > goal//10: continue
        a[x] += y*11

for i,x in enumerate(a):
    if x >= goal:
        print(i) #part 1
        break
