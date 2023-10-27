a="""jio a 19
inc a
tpl a
inc a
tpl a
inc a
tpl a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp 23
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
jio a 8
inc b
jie a 4
tpl a
inc a
jmp 2
hlf a
jmp -7"""

test="""inc a
jio a 2
tpl a
inc a"""
#a=test
#a = a.replace(",","").replace("+","")
b=[x.split() for x in a.splitlines()]
for x in b: print(x)

def part(p):
    r={x:0 for x in "ab"}
    i=0
    r["a"] += p-1
    while True:
        if i<0:break
        try: 
            instr = b[i]
            print(i,r,b[i])
        except: break
        op, x = instr[:2]
        if len(instr) == 3:
            y = instr[2]
        if op == "hlf": r[x] //= 2
        if op == "tpl": r[x] *= 3
        if op == "inc": r[x] += 1
        if op == "jmp": 
            i += int(x)
            continue
        if op == "jie":
            xVal = r[x] if x in r else int(x)
            if xVal % 2 == 0:
                i += int(y)
                continue
        if op == "jio":
            xVal = r[x] if x in r else int(x)
            if xVal == 1:
                i += int(y)
                continue
        i+=1
    print(r["b"])
part(1)
part(2)