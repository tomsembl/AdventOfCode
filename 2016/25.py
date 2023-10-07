a="""cpy a d
cpy 15 c
cpy 170 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21"""

def doTheThing():
    for inp in range(10000):
        #print(inp)
        b=[x.split() for x in a.splitlines()]
        r={x:0 for x in "abcd"}
        r2=[]
        r["a"]=inp
        i=0
        winCondition = False
        printing = False
        while True:
            try: instr = b[i]
            except: break
            op, x = instr[:2]
            if len(instr) == 3:
                y = instr[2]
            
            # if i==20: 
            #     print(instr,r)
            #     printing = True
            # if i<20:
            #     printing = False
            # if printing:
            #     print(instr,r)
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
            if op == "out": 
                if r2 and r2[-1] != 1-r[x]: break
                r2.append(r[x])
                if r2[0] != 0: break
                if len(r2) > 100:
                    winCondition = True
                    break
                #print(r2)
            i+=1
        if winCondition:
            print(inp)
            break
    
doTheThing()
#i=13
# x + 2550 // 2