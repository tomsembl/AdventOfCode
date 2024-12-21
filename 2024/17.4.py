a="""Register A: 61657405
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0"""
test="""Register A: 0 
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
test="""Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
#a=test
b=[x for x in a.splitlines()]
registers = [int(x.split(": ")[1]) for x in b[:3]]
program = [int(x) for x in b[4].split(": ")[1].split(",")]
print(registers,program)

bestOutput = []
bestOutLen = 0
def listStartsWithList(l1,l2):
    global bestOutput,bestOutLen,j
    for i in range(len(l2)):
        if l1[i] != l2[i]:
            if i-1 > bestOutLen:
                bestOutLen = i-1
                bestOutput = l2[:i]
                print("bestOutput",bestOutput,j,registers)
                
            return False
    return True

j=526
outputs=[]
nInvalidOutputs = 0
while outputs != program:
    i = 0
    j+=1
    print(f"j {j}")
    if j % 100000 == 0:
        print(j,nInvalidOutputs)
    # if j == 117440:
    #     print("j == 117440")
    outputs=[]
    registers = [int(x.split(": ")[1]) for x in b[:3]]
    registers[0] = j
    while i < len(program)-1:
        if not listStartsWithList(program,outputs):
            nInvalidOutputs += 1
            break
        opcode, operand = program[i:i+2]
        if 3 < operand < 7:
            operand = registers[operand-4]
        # if operand == 7:
        #     print("invalid operand 7")
        #     break
        
        if opcode == 0: #adv
            print(f"op 0: A: {bin(registers[0])[2:]} // 8 = {bin(registers[0] //  (2 ** operand))[2:]}")
            registers[0] = registers[0] //  (2 ** operand)
        if opcode == 1: #bxl
            print(f"op 1: B: {bin(registers[1])[2:]} XOR 10 = {bin(registers[1] ^ operand)[2:]}")
            registers[1] = registers[1] ^ operand
        if opcode == 2: #bst
            print(f"op 2: B = A: {bin(registers[0])[2:]} % 8 = {bin(operand % 8)[2:]}")
            registers[1] = operand % 8
        if opcode == 3: #jnz
            print(f"jump to 0")
            if registers[0] != 0:
                i = operand
                continue
        if opcode == 4: #bxc
            print(f"op 4: B: {bin(registers[1])[2:]} XOR C: {bin(registers[2])[2:]} = {bin(registers[1] ^ registers[2])[2:]}")
            registers[1] = registers[1] ^ registers[2]
        if opcode == 5: #out
            print(f"op 5: output B: {bin(registers[1])[2:]} % 8 = {bin(operand % 8)[2:]}")
            outputs.append(operand % 8)
        if opcode == 6: #bdv
            print(f"op 6: C = A: {bin(registers[0])[2:]} // 2^B: {bin(operand)[2:]} = {bin(registers[0] //  (2 ** operand))[2:]}")
            registers[1] = registers[0] //  (2 ** operand)
        if opcode == 7: #cdv
            print(f"op 7: C = A: {bin(registers[0])[2:]} // 2^B: {bin(operand)[2:]} = {bin(registers[0] //  (2 ** operand))[2:]}")
            registers[2] = registers[0] //  (2 ** operand)
            
            
            
        #print(opcode,operand)
        i += 2
    #print(outputs)
    #print(registers)
    #print(",".join([str(x) for x in outputs]))
print(j) #p2

# 2,4
    # B = A % 8
# 1,2
    # B = B ^ 2
# 7,5
    # C = A //  (2 ** B)
# 4,3
    # B = B ^ C
# 0,3
    # A = A //  (2 ** 3)
# 1,7
    # B = B ^ 7
# 5,5
    # outputs.append(B % 8)
# 3,0
    # If A != 0, repeat (i = 0)
    
    
# (A % 8) ^ 2