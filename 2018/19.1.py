a="""#ip 3
addi 3 16 3
seti 1 2 5
seti 1 3 2
mulr 5 2 1
eqrr 1 4 1
addr 1 3 3
addi 3 1 3
addr 5 0 0
addi 2 1 2
gtrr 2 4 1
addr 3 1 3
seti 2 5 3
addi 5 1 5
gtrr 5 4 1
addr 1 3 3
seti 1 2 3
mulr 3 3 3
addi 4 2 4
mulr 4 4 4
mulr 3 4 4
muli 4 11 4
addi 1 6 1
mulr 1 3 1
addi 1 21 1
addr 4 1 4
addr 3 0 3
seti 0 3 3
setr 3 4 1
mulr 1 3 1
addr 3 1 1
mulr 3 1 1
muli 1 14 1
mulr 1 3 1
addr 4 1 4
seti 0 3 0
seti 0 7 3"""
test="""#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5"""
#a=test
reg = [1,0,0,0,0,0]
ip = int(a.splitlines()[0][-1])
instructions=[[int(x) if x.isnumeric() else x for x in y.split()] for y in a.splitlines()[1:]]

def edit(arr, pos, value):
    arrCopy = arr[::]
    arrCopy[pos] = value
    return arrCopy

addr = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] + reg[inst[1]] )
addi = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] + inst[1] )
mulr = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] * reg[inst[1]] )
muli = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] * inst[1] )
banr = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] & reg[inst[1]] )
bani = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] & inst[1] )
borr = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] | reg[inst[1]] )
bori = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] | inst[1] )
setr = lambda reg,inst: edit(reg, inst[2], reg[inst[0]] )
seti = lambda reg,inst: edit(reg, inst[2], inst[0] )
gtir = lambda reg,inst: edit(reg, inst[2], int(inst[0] > reg[inst[1]]) )
gtri = lambda reg,inst: edit(reg, inst[2], int(reg[inst[0]] > inst[1]) )
gtrr = lambda reg,inst: edit(reg, inst[2], int(reg[inst[0]] > reg[inst[1]]) )
eqir = lambda reg,inst: edit(reg, inst[2], int(inst[0] == reg[inst[1]]) )
eqri = lambda reg,inst: edit(reg, inst[2], int(reg[inst[0]] == inst[1]) )
eqrr = lambda reg,inst: edit(reg, inst[2], int(reg[inst[0]] == reg[inst[1]]) )
ops = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
opNames = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]

ipCounts={x:0 for x in range(len(instructions))}
while True:
    try: opName,a,b,c = instructions[reg[ip]]
    except IndexError: break
    ipCounts[reg[ip]] += 1
    op = ops[opNames.index(opName)]
    if reg[ip] == 3 and reg[3] != 0:
        print(reg[4]) #copy this output to clipboard
        break
    reg = op(reg,(a,b,c))
    reg[ip]+=1
# paste the number from reg[4] into here:
# https://allmathsymbols.com/sum-of-factors-calculator/
# answer to part 2 is sum of factors