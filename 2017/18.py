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
test="""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
#a=test
b=[x.split() for x in a.splitlines()]
regs=[{chr(x):0 for x in range(97,97+26)} for _ in range(2)]
for x in range(2): regs[x]["p"] = x
i=[0,0]
q={x:[] for x in range(2)}
dead=[False,False]
total=0
while True:
    if all(dead): 
        break
    dead=[False,False]
    for p in range(2):
        if dead[p]: continue
        try:
            instr=b[i[p]]
        except:
            dead[p]=True
        op, adr = instr[0], instr[1]
        if len(instr)==3:
            n=instr[2]
            if n[0]=="-" or n.isnumeric(): n=int(n)
            n = n if type(n)==int else regs[p][n]
        if op == "snd":
            q[1-p].append(regs[p][adr] if not adr.isnumeric() else int(adr))
            if p==1: total += 1
        if op == "set":
            regs[p][adr] = n
        if op == "add":
            regs[p][adr] += n
        if op == "mul":
            regs[p][adr] *= n
        if op == "mod":
            regs[p][adr] %= n
        if op == "rcv":
            try:
                regs[p][adr] = q[p].pop(0)
            except: 
                dead[p] = True
                continue
        if op == "jgz":
            adr = int(adr) if adr.isnumeric() else regs[p][adr]
            if adr > 0:
                i[p]+=n
                continue
        i[p]+=1
print(total)
#125723 too high
#125476 too high