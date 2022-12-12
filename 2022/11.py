divisible = lambda x,y: x % y == 0
monkeys = [{
    "Starting items": [91, 54, 70, 61, 64, 64, 60, 85],
    "Operation": (lambda new : new * 13),
    "Test": 2,
    "If true": 5,
    "If false": 2
},
{
    "Starting items": [82],
    "Operation": (lambda new : new + 7),
    "Test": 13,
    "If true": 4,
    "If false": 3,
},
{
    "Starting items": [84, 93, 70],
    "Operation": (lambda new : new + 2),
    "Test": 5,
    "If true": 5,
    "If false": 1
},
{
    "Starting items": [78, 56, 85, 93],
    "Operation": (lambda new : new * 2),
    "Test": 3,
    "If true": 6,
    "If false": 7
},
{
#Monkey 4:
    "Starting items":[ 64, 57, 81, 95, 52, 71, 58],
    "Operation": (lambda new : new * new),
    "Test": 11,
    "If true": 7,
    "If false": 3
},
{
#Monkey 5:
    "Starting items":[58, 71, 96, 58, 68, 90],
    "Operation": (lambda new : new + 6),
    "Test": 17,
    "If true": 4,
    "If false": 1
},
{
#Monkey 6:
    "Starting items": [56, 99, 89, 97, 81],
    "Operation": (lambda new : new + 1),
    "Test": 7,
    "If true": 0,
    "If false": 2
},
{
#Monkey 7:
    "Starting items": [68, 72],
    "Operation": (lambda new : new + 8),
    "Test": 19,
    "If true": 6,
    "If false": 0
}]

test = [
    {
    #Monkey 0:
    "Starting items": [79, 98],
    "Operation": (lambda new : new * 19),
    "Test": 23,
    "If true":  2,
    "If false":  3
    },{
#Monkey 1:
    "Starting items": [54, 65, 75, 74],
    "Operation": (lambda new : new + 6),
    "Test": 19,
    "If true":  2,
    "If false":  0
    },{

#Monkey 2:
    "Starting items": [79, 60, 97],
    "Operation": (lambda new : new * new),
    "Test": 13,
    "If true": 1,
    "If false":  3
    },{

#Monkey 3:
    "Starting items": [74],
    "Operation": (lambda new : new + 3),
    "Test": 17,
    "If true":  0,
    "If false":  1
    }
]
#monkeys=test
factors=list(set([x["Test"] for x in monkeys]))
mod = 1
for x in factors: mod *= x
n=len(monkeys)
print(factors)

counts=[0 for _ in range(8)]
for round in range(10000): #20
    for j in range(n):
        monkey=monkeys[j]
        operation  = monkey["Operation"]
        test = lambda x : divisible(x,monkey["Test"])
        trueFalse = [monkey["If true"],monkey["If false"]]
        for _ in range(len(monkeys[j]["Starting items"])):
            item = monkeys[j]["Starting items"].pop()
            counts[j]+=1 # increment inspection count
            item = operation(item)
            item = item % mod       #part 2
            #worry = worry // 3     #part 1
            testBool = test(item)
            throwTo = trueFalse[0] if testBool else trueFalse[1]
            monkeys[throwTo]["Starting items"]=monkeys[throwTo]["Starting items"]+[item]
print(sorted(counts)[::-1][:2])
