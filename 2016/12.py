a="""cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 12 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""
test="""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""
#a=test
b=[x.split() for x in a.splitlines()]
def part(p):
    r={x:0 for x in "abcd"}
    r["c"]=p-1#part 2
    i=0
    while True:
        #print(i,r)
        try: instr = b[i]
        except: break
        op, x = instr[:2]
        if len(instr) == 3:
            y = instr[2]
        if op == "cpy":
            xVal = r[x] if x in r else int(x)
            r[y] = xVal
        if op == "inc": r[x] += 1
        if op == "dec": r[x] -= 1
        if op == "jnz": 
            xVal = r[x] if x in r else int(x)
            if xVal != 0:
                i += int(y)
                continue
        i+=1
    print(r["a"])
part(1)
part(2)