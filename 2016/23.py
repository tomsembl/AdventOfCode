a="""cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 77 c
jnz 87 d
inc a
inc d
jnz d -2
inc c
jnz c -5"""
test="""cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""
#a=test
toggles={1:{"inc":"dec", "dec":"inc", "cpy":"inc", "jnz":"inc", "tgl":"inc"},
         2:{"jnz":"cpy", "dec":"jnz", "cpy":"jnz", "inc":"jnz", "tgl":"jnz"}}
def part(p):
    b=[x.split() for x in a.splitlines()]
    toggled=set()
    r={x:0 for x in "abcd"}
    r["a"]=7 if p==1 else 12
    i=0
    while True:
        #print(i,r)
        try: instr = b[i]
        except: break
        try:
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
                    i += (r[y] if y in r else int(y))
                    continue
            if op == "tgl": 
                ii = i+(r[x] if x in r else int(x))
                tglInstr = b[ii]
                b[ii][0] = toggles[len(tglInstr)-1][tglInstr[0]]
                toggled.add(ii)
        except: pass
        i+=1
    print(r["a"])
part(1)
part(2)