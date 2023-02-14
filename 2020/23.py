a="942387615"
test="389125467"
#a=test
b=[int(x) for x in a]
dic={}
for i,x in enumerate(b):
    dic[x]={"prev":b[i-1],"next":b[(i+1)%9]}
print(a)
for x in dic:
    print(x,dic[x])
current=b[0]
n=9
for _ in range(100):
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
string = ""
for x in range(8):
    node = dic[node]["next"]
    string+= str(node)

print(string) #part1