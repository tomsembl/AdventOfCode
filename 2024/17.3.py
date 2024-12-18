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
bestOutLen = 0
def listStartsWithList(l1,l2):
    global bestOutput,bestOutLen,i
    for j in range(len(l2)):
        if l1[j] != l2[j]:
            if j-1 > bestOutLen:
                bestOutLen = j-1
                bestOutput = l2[:j-1]
                print("bestOutput",bestOutput,i)
                
            return False
    return True
 
outputs=[]
i = -1
while program != outputs:
    i+=1
    A = i
    B=0
    C=0
    outputs=[]
    while A != 0 and listStartsWithList(program,outputs):
        B = A % 8
        B = B ^ 2
        C = A // (2 ** B)
        B = B ^ C
        A = A // 8
        B = B ^ 7
        outputs.append(B % 8)
print(A)