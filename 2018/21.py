a="""#ip 4
seti 123 0 2
bani 2 456 2
eqri 2 72 2
addr 2 4 4
seti 0 0 4
seti 0 8 2
bori 2 65536 5
seti 2238642 0 2
bani 5 255 3
addr 2 3 2
bani 2 16777215 2
muli 2 65899 2
bani 2 16777215 2
gtir 256 5 3
addr 3 4 4
addi 4 1 4
seti 27 3 4
seti 0 8 3
addi 3 1 1
muli 1 256 1
gtrr 1 5 1
addr 1 4 4
addi 4 1 4
seti 25 4 4
addi 3 1 3
seti 17 2 4
setr 3 9 5
seti 7 9 4
eqrr 2 0 3
addr 3 4 4
seti 5 0 4"""
reg = [0,0,0,0,0,0]
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

reg=[127131,0,0,0,0,0]#127131 too low
for i,x in enumerate(instructions):
    print(i,x)
ipCounts={x:0 for x in range(len(instructions))}
r2 = 99999999999999999
while True:
    if reg[2] <= r2 and reg[2] not in [123,72,1,0]: 
        r2=reg[2]
        #print(r2)
    #print(reg[4],reg[:4]+[""]+reg[5:])
    try: opName,a,b,c = instructions[reg[ip]]
    except IndexError: break
    ipCounts[reg[ip]] += 1
    op = ops[opNames.index(opName)]
    reg = op(reg,(a,b,c))
    reg[ip]+=1

r0,r1,r2,r3,r5 =0,0,0,0,0
i=6
r5 = r2 | 65536 #6
r2 = 2238642    #7
r3 = r5 & 255   #8
r2 += r3        #9
r2 &= 16777215  #10
r2 *= 65899     #11
r2 &= 16777215  #12
r3 = int(256>r5)#13
i  += r3        #14
i  += 1         #15
i  = 27         #16
r3 = 0          #17
r1 = r3 + 1     #18
r1 *= 256       #19
r1 = int(r1>r5) #20
i  += r1        #21
i  += 1         #22
i  = 25         #23
r3 += 3         #24
i  = 17         #25
r5 = r3         #26
i  = 7          #27
r3 = int(r2==r0)#28
i += r3         #29
r4 = r5 + 1     #30

