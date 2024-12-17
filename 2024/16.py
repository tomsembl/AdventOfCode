a="""Register A: 61657405
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0"""
test="""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
b=[x for x in a.splitlines()]
registers = [int(x.split(": ")[1]) for x in b[:3]]
program = [int(x) for x in b[4].split(": ")[1].split(",")]

i = 0
outputs=[]
while i < len(program)-1:
    opcode, operand = program[i:i+2]
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
            i = operand
            continue
    if opcode == 4: #bxc
        registers[1] = registers[1] ^ registers[2]
    if opcode == 5: #out
        outputs.append(operand % 8)
    if opcode == 6: #bdv
        registers[1] = registers[0] //  (2 ** operand)
    if opcode == 7: #cdv
        registers[2] = registers[0] //  (2 ** operand)

    i += 2
print(",".join([str(x) for x in outputs])) #p1