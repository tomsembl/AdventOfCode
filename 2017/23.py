a="""set b 65
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""
b=[x.split() for x in a.splitlines()]
regs={chr(x):0 for x in range(97,97+8)}
regs["a"]=1
dead=[False,False]
total=0
i=0
last = regs["b"]
while True:
    try: 
        instr=b[i]
        if regs["b"] != last:
            last = regs["b"]
            print(regs,i, instr)
    except: 
        break
    op, c, d = instr
    if c[0]=="-" or c.isnumeric(): c=int(c)
    if d[0]=="-" or d.isnumeric(): d=int(d)
    d = d if type(d)==int else regs[d]
    if op == "set":
        regs[c] = d
    if op == "sub":
        if d == -1 and i == 16:
            regs[c] = regs["b"]
            i+=1
            continue
        regs[c] -= d
    if op == "mul":
        regs[c] *= d
        total+=1
    if op == "jnz":
        c = c if type(c)==int else regs[c]
        if c != 0:
            i+=d
            continue
    i+=1
print(total)#part 1
print(regs["h"])#part 2

#123500 too high
#500 too low
#501 too low