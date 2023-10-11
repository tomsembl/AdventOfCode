a="hepxcrrq"
test=""
#a=test
bads=[ord(x)-97 for x in "iol"]
triples=[z for z in [[y for y in range(x,x+3)] for x in range(26-2)] if not any([zz in z for zz in bads])]
stringify = lambda y: "".join([chr(x+97) for x in y])
triplesStr = [stringify(x) for x in triples]
intify = lambda y: [ord(x)-97 for x in y]

def increment(lst):
    lst[-1] += 1
    while 26 in lst:
        for i in range(len(lst)-1,-1,-1):
            if lst[i] == 26:
                lst[i] = 0
                if i>0:
                    lst[i-1] += 1
    return lst

def isValid(x):
    for b in bads:
        if b in x: return False
    string=stringify(x)
    if not any([y in string for y in triplesStr]):
        return False
    last=None
    doubles=set()
    for y in x:
        if y==last:
            doubles.add(y)
            last = None
        last = y
    if len(doubles) < 2: return False
    return True

ints=intify(a)
while not isValid(ints):
    ints=increment(ints)
print(stringify(ints))
ints=increment(ints)
while not isValid(ints):
    ints=increment(ints)
print(stringify(ints))