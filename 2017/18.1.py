a="""set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 735
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""
test="""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
#a=test
b=[x.split() for x in a.splitlines()]
reg={chr(x):0 for x in range(97,97+26)}
lastSound=None
i=0
while True:
    instr=b[i]
    op, adr = instr[0], instr[1]
    if len(instr)==3:
        n=instr[2]
        if n[0]=="-" or n.isnumeric(): n=int(n)
        n = n if type(n)==int else reg[n]
    if op == "snd":
        lastSound = reg[adr]
    if op == "set":
        reg[adr] = n
    if op == "add":
        reg[adr] += n
    if op == "mul":
        reg[adr] *= n
    if op == "mod":
        reg[adr] %= n
    if op == "rcv":
        if n!=0:
            print(lastSound)#part 1
            break
    if op == "jgz":
        if reg[adr]>0:
            i+=n
            continue
    i+=1
    print(i,reg)