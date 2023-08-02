input = 323081
target = 10
b=[3,7]
c=[0,1]
while target > len(b) - input:
    b += [int(x) for x in str(sum([b[y] for y in c]))]
    c = [(x + b[x]+1) % len(b) for x in c]
print("".join([str(x) for x in b[input:input+target]])) #part 1

input = 323081
test = 51589
#input = test
listInput = list(map(int,str(input)))
lenInput = len(listInput)
b=[3,7]
c=[0,1]
cleanEnd=False
while True:
    b += [int(x) for x in str(sum([b[y] for y in c]))]
    c = [(x + b[x]+1) % len(b) for x in c]
    if (cleanEnd := b[-lenInput:] == listInput) or b[-lenInput - 1: -1] == listInput: break
print(len(b) - lenInput - (0 if cleanEnd else 1)) #part 2