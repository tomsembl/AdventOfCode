a=314
test=3
#a=test
b=[]
i=0
l=0
iterations = 2018
for x in range(iterations):
    b.insert(i,x)
    l+=1
    if x == iterations-1:
        break
    i = ((i+a) % l) + 1
print(b[i+1]) #part 1

b=[]
i=0
l=0
iterations = 50_000_000
pos1=None
for x in range(iterations):
    if i==1:pos1=x
    l+=1
    if x == iterations-1:
        break
    i = ((i+a) % l) + 1
print(pos1) #part 1
