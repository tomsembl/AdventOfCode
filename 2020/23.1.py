a="942387615"
test="389125467"
#a=test
b=[int(x) for x in a]
dic={}
for i,x in enumerate(b):
    dic[x]={"prev":b[i-1],"next":b[(i+1)%9]}
current=b[0]

n=1_000_000
firstCup,lastCup = b[0],b[-1]
dic[lastCup]["next"]=10
for x in range(10,n+1):
    dic[x]={"prev":x-1,"next":x+1}
dic[10]["prev"] = lastCup
dic[1_000_000]["next"] = firstCup

for j in range(10_000_000):
    if not j%100_000: print(j)
    pickupStart = dic[current]["next"]
    pickupMid = dic[pickupStart]["next"]
    pickupEnd = dic[pickupMid]["next"]
    pickup = (pickupStart, pickupMid, pickupEnd)
    pickupNext = dic[pickupEnd]["next"]
    start=True
    destination=current
    while start or destination in pickup:
        start=False
        if destination == 1: destination = n
        else: destination -= 1
    destinationNext = dic[destination]["next"]
    dic[current]["next"] = pickupNext
    dic[pickupNext]["prev"] = current
    dic[destination]["next"] = pickupStart
    dic[destinationNext]["prev"] = pickupEnd
    dic[pickupEnd]["next"] = destinationNext
    dic[pickupStart]["prev"] = destination
    current = dic[current]["next"]

node = 1
final = []
for x in range(2):
    node = dic[node]["next"]
    final.append(node)

print(final[0] * final[1]) #part2