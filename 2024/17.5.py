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
winners = []
for x in range(len(program)):
    leastsignificants = sum([z<<(i*3) for i,z in enumerate(winners)])
    for y in range(64*8):
        registers = [int(x.split(": ")[1]) for x in b[:3]]
        #print(bin((y << (x * 3))))
        registers[0] = (y << (x * 3)) + leastsignificants
        i = 0
        outputs=[]
        while i < len(program)-1:
            opcode, operand = program[i:i+2]
            if 3 < operand < 7:
                operand = registers[operand-4]
            
            if opcode == 0: #adv
                print(f"    op 0: A: {bin(registers[0])[2:]} // 8 = {bin(registers[0] //  (2 ** operand))[2:]}")
                registers[0] = registers[0] //  (2 ** operand)
            if opcode == 1: #bxl
                print(f"    op 1: B: {bin(registers[1])[2:]} XOR 10 = {bin(registers[1] ^ operand)[2:]}")
                registers[1] = registers[1] ^ operand
            if opcode == 2: #bst
                print(f"    op 2: B = A: {bin(registers[0])[2:]} % 8 = {bin(operand % 8)[2:]}")
                registers[1] = operand % 8
            if opcode == 3: #jnz
                print(f"    jump to 0")
                if registers[0] != 0:
                    i = operand
                    continue
            if opcode == 4: #bxc
                print(f"    op 4: B: {bin(registers[1])[2:]} XOR C: {bin(registers[2])[2:]} = {bin(registers[1] ^ registers[2])[2:]}")
                registers[1] = registers[1] ^ registers[2]
            if opcode == 5: #out
                print(f"    op 5: output B: {bin(registers[1])[2:]} % 8 = {bin(operand % 8)[2:]}")
                outputs.append(operand % 8)
            if opcode == 6: #bdv
                print(f"    op 6: C = A: {bin(registers[0])[2:]} // 2^B: {bin(operand)[2:]} = {bin(registers[0] //  (2 ** operand))[2:]}")
                registers[1] = registers[0] //  (2 ** operand)
            if opcode == 7: #cdv
                print(f"    op 7: C = A: {bin(registers[0])[2:]} // 2^B: {bin(operand)[2:]} = {bin(registers[0] //  (2 ** operand))[2:]}")
                registers[2] = registers[0] //  (2 ** operand)

            i += 2
        print(f"x={x}, y={y}, outputs = {outputs}, A = {bin((y << (x * 3)) + leastsignificants)[2:]}")
        if len(outputs) >= x+2:
            if outputs[:x+2] == program[:x+2]:
                winners.append(y)
                print(f"winner: {y}")