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
ip = int(a.splitlines()[0][-1])
instructions=[[int(x) if x.isnumeric() else x for x in y.split()] for y in a.splitlines()[1:]]


addr = lambda i,a,b,c:  f"r[{c}] = r[{a}] + r[{b}] "
addi = lambda i,a,b,c:  f"r[{c}] = r[{a}] + {b} "
mulr = lambda i,a,b,c:  f"r[{c}] = r[{a}] * r[{b}] "
muli = lambda i,a,b,c:  f"r[{c}] = r[{a}] * {b} "
banr = lambda i,a,b,c:  f"r[{c}] = r[{a}] & r[{b}] "
bani = lambda i,a,b,c:  f"r[{c}] = r[{a}] & {b} "
borr = lambda i,a,b,c:  f"r[{c}] = r[{a}] | r[{b}] "
bori = lambda i,a,b,c:  f"r[{c}] = r[{a}] | {b} "
setr = lambda i,a,b,c:  f"r[{c}] = r[{a}] "
seti = lambda i,a,b,c:  f"r[{c}] = {a} "
gtir = lambda i,a,b,c:  f"r[{c}] = int({a} > r[{b}]) "
gtri = lambda i,a,b,c:  f"r[{c}] = int(r[{a}] > {b}) "
gtrr = lambda i,a,b,c:  f"r[{c}] = int(r[{a}] > r[{b}]) "
eqir = lambda i,a,b,c:  f"r[{c}] = int({a} == r[{b}]) "
eqri = lambda i,a,b,c:  f"r[{c}] = int(r[{a}] == {b}) "
eqrr = lambda i,a,b,c:  f"r[{c}] = int(r[{a}] == r[{b}]) "
ops = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
opNames = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]

instructions2 = []
for i,x in enumerate(instructions):
    opName,a,b,c = x
    op = ops[opNames.index(opName)]
    instr = op(i,a,b,c)
    instructions2.append(instr)

instructions2[17]="r[3] = 255"
# for i,x in enumerate(instructions2):
#     print(f"{i}:",x)
r = [0,0,0,0,0,0]
ii = 0
firstR2 = None
lastR2 = None
seen = set()
while True:
    if not 0 <= r[4] <= 30: break
    instr = instructions2[r[4]]
    if r[4] == 17:# and ii==0:
        ii+=1
        instr = f"r[3] = {int(r[5]/256)-1}"
    if r[4]==28:
        if not firstR2: firstR2 = r[2] 
        if r[2] in seen:
            break
        lastR2 = r[2]
        seen.add(r[2])
    # print(r[:4]+[" "]+r[5:],f"{r[4]}:",instr)
    # print()
    exec(instr)
    r[4]+=1
print(firstR2)#part 1
print(lastR2)#part 2

#6823672 too high
#206 too low
# 0: r[2] = 123 
# 1: r[2] = r[2] & 456
# 2: r[2] = int(r[2] == 72)
# 3: r[4] = r[2] + r[4]
# 4: r[4] = 0
# 5: r[2] = 0
# 6: r[5] = r[2] | 65536
# 7: r[2] = 2238642
# 8: r[3] = r[5] & 255
# 9: r[2] = r[2] + r[3]
# 10: r[2] = r[2] & 16777215
# 11: r[2] = r[2] * 65899
# 12: r[2] = r[2] & 16777215
# 13: r[3] = int(256 > r[5])
# 14: r[4] = r[3] + r[4]
# 15: r[4] = r[4] + 1
# 16: r[4] = 27
# 17: r[3] = 0
# 18: r[1] = r[3] + 1
# 19: r[1] = r[1] * 256
# 20: r[1] = int(r[1] > r[5])
# 21: r[4] = r[1] + r[4]
# 22: r[4] = r[4] + 1
# 23: r[4] = 25
# 24: r[3] = r[3] + 1
# 25: r[4] = 17
# 26: r[5] = r[3]
# 27: r[4] = 7
# 28: r[3] = int(r[2] == r[0])
# 29: r[4] = r[3] + r[4]
# 30: r[4] = 5