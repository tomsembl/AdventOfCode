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
 
def f(i):
    prog=0
    outputs=[]
    registers=[i,0,0]
    while prog < len(program)-1:
        opcode, operand = program[prog:prog+2]
        if 3 < operand < 7:
            operand = registers[operand-4]
        
        if opcode == 0: #adv
            registers[0] = registers[0] //  (2 ** operand)
        if opcode == 1: #bxl
            registers[1] = registers[1] ^ operand
        if opcode == 2: #bst
            registers[1] = operand % 8
        if opcode == 3: #jnz
            if registers[0] != 0:
                prog = operand
                continue
        if opcode == 4: #bxc
            registers[1] = registers[1] ^ registers[2]
        if opcode == 5: #out
            outputs.append(operand % 8)
        if opcode == 6: #bdv
            registers[1] = registers[0] //  (2 ** operand)
        if opcode == 7: #cdv
            registers[2] = registers[0] //  (2 ** operand)

        prog += 2
    return outputs

winners = []
for x in range(len(program)):
    for y in range(8):
        wins = sum([z<<((i+1)*3) for i,z in enumerate(winners[::-1])])
        num = wins + y
        fnum = f(num)
        print(x,y,bin(num)[2:],",".join([str(x) for x in fnum]))
        if len(fnum) < x+1:
            continue
        if fnum[-(x+1):] == (program)[-(x+1):]:
            winners.append(y)
            print(f"winner {y}")
            break
    if len(winners) == x:
        winners.append(0)
        
    
#1890242470951951 too high