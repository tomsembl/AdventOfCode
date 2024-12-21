a="""Register A: 61657405
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0"""
# test="""Register A: 0 
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""
# test="""Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""
#a=test
b=[x for x in a.splitlines()]
program = [int(x) for x in b[4].split(": ")[1].split(",")]

bestOutput = []
bestOutLen = -1
def listStartsWithList(l1,l2,i):
    global bestOutput,bestOutLen
    for j in range(len(l2)):
        if l1[j] != l2[j]:
            if j-1 > bestOutLen:
                bestOutLen = j-1
                bestOutput = l2[:j]
                #print("bestOutput",bestOutput,i, bin(i)[2:])
                
            return False
    return True
 
i = -1
def f(i):
    A = i
    B=0
    C=0
    outputs=[]
    while A != 0 and listStartsWithList(program,outputs,i):
        B = A % 8
        B = B ^ 2
        C = A // (2 ** B)
        B = B ^ C
        A = A // 8
        B = B ^ 7
        outputs.append(B % 8)
    return outputs

winners = []
for x in range(len(program)-1):
    
    for y in range(8):
        num = (y << (3 * (x))) + sum([z<<(i*3) for i,z in enumerate(winners)])
        fnum = f(num)
        print(x,y,bin(num)[2:],fnum)
        if len(fnum) < x+1:
            continue
        if fnum[:x+1] == program[:x+1]:
            winners.append(y)
            break
    if len(winners) == x:
        winners.append(0)
#print(f(17120271))