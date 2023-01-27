a="""inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -2
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y"""
ops=["inp","add","mul","div","mod","eql"]
instr=[[int(y) if y.isnumeric() or "-" in y else y for y in x.split()]+([-1] if x[0]=="i" else []) for x in a.splitlines() if x[0]!="#"]
instr=[[ops.index(op),"wxyz".index(a),c:=type(b)==int,b if c else "wxyz".index(b)] for op,a,b in instr]

def runOps(input,outputDic=False):
    dic={0:0,1:0,2:0,3:0}
    i=0
    for x in instr: 
        op,a,c,b = x
        if op == 0: 
            dic[a] = int(input[i])
            i+=1
        elif op == 1: dic[a] += b if c else dic[b]
        elif op == 2: dic[a] *= b if c else dic[b]
        elif op == 3: 
            if b!= 0: dic[a] //= b if c else dic[b]
            else: print("div0"); break
        elif op == 4: dic[a] %= b if c else dic[b]
        elif op == 5: dic[a] = 1 if (b if c else dic[b]) == dic[a] else 0
    if outputDic: return dic
    return dic[3]

def isInput(x): return all([x[0]=="i", x[1:].isnumeric(), len(x) in [2,3]])

def getType(a,b):
    if (AisVar := a in ["w","x","y","z"]): a = dic[a]
    if (BisVar := b in ["w","x","y","z"]): b = dic[b]
    AisInt,BisInt = type(a) == int, type(b) == int
    if AisInt and BisInt: return a,b,AisInt,BisInt, False, False
    a,b = str(a),str(b)
    #AisEquation, BisEquation = "(" in a, "(" in b
    AisInput, BisInput = isInput(a), isInput(b)
    return a,b,AisInt,BisInt,AisInput,BisInput#,AisEquation,BisEquation

def execRange1to9(a,b,equationStr,AisInt):
    answers=[]
    for i in range(1,10):
        s = equationStr
        for j in range(14):
            s = s.replace(f"i{j}",str(i))
        answers.append(eval(s))
    if len(set(answers)) == 1: return answers[0],True
    return None,False

dic={"w":0,"x":0,"y":0,"z":0}
ops=["inp","add","mul","div","mod","eql"]
def generateEquation():
    i=0
    rowCount=0
    for op,a,c,b in instr:
        rowCount+=1 
        a="wxyz"[a]
        if not c: b="wxyz"[b]
        print(f"\n{rowCount}: {ops[op]} {a} {b}")
        
        if op == 0:  #inp
            dic[a] = f"i{i}"
            i+=1
            print(f"answer:{dic[a]}")

        elif op == 1: #add
            add = (b if c else dic[b])
            valA, add, AisInt, BisInt, AisInput, BisInput = getType(dic[a],add)
            if valA in [0,'0']: dic[a] = add ; print(f"{valA} {add}, answer:{dic[a]}") ; continue
            if AisInt and BisInt: dic[a] = valA + add
            else: dic[a] = f"({valA}) + ({add})"
            print(f"{valA} {add}, answer:{dic[a]}")

        elif op == 2: #mul
            mul = (b if c else dic[b])
            valA, mul, AisInt, BisInt, AisInput, BisInput = getType(dic[a],mul)
            if valA in [0,'0'] or mul in [1,'1']: print(f"{valA} {mul}, answer:{dic[a]}") ; continue
            if mul in [0,'0']: dic[a] = 0 ; print(f"{valA} {mul}, answer:{dic[a]}") ; continue
            if AisInt and BisInt: dic[a] = valA * mul
            else: dic[a] = f"({valA}) * ({mul})"
            print(f"{valA} {mul}, answer:{dic[a]}")

        elif op == 3: #div
            div = (b if c else dic[b])
            valA, div, AisInt, BisInt, AisInput, BisInput = getType(dic[a],div)
            if valA in [0,'0'] or div in [1,'1']: print(f"{valA} {div}, answer:{dic[a]}") ; continue
            if div in [0,'0']: print("div0"); print(f"{valA} {div}, answer:{dic[a]}") ; break
            if AisInt and BisInt: dic[a] = valA // div
            else: dic[a] = f"({valA}) // ({div})"
            print(f"{valA} {div}, answer:{dic[a]}")

        elif op == 4: #mod
            mod = (b if c else dic[b])
            valA, mod, AisInt, BisInt, AisInput, BisInput = getType(dic[a],mod)
            if valA in [0,'0'] or mod in [0,'0']: print(f"{valA} {mod}, answer:{dic[a]}") ; continue
            if AisInt and BisInt: dic[a] = valA % mod
            else: dic[a] = f"({valA}) % ({mod})"
            print(f"{valA} {mod}, answer:{dic[a]}")

        elif op == 5: #eql
            eql = (b if c else dic[b])
            valA, eql, AisInt, BisInt, AisInput, BisInput = getType(dic[a],eql)
            if valA in [0,'0'] or eql in [1,'1']: print(f"{valA} {eql}, answer:{dic[a]}") ; continue
            if AisInt and BisInt: dic[a] = int(valA == eql)
            else: 
                equationStr = f"({valA}) == ({eql})"
                if valA == eql: dic[a] = 1 #strings match
                elif isInput(eql): #if eql is an input, try range 1-9 with exec
                    answer, isAlways = execRange1to9(valA,eql,equationStr,AisInt)
                    if isAlways: 
                        if type(answer)==bool: 
                            answer = int(answer)
                        dic[a] = answer
                    else: dic[a] = equationStr
                else: dic[a] = equationStr
            print(f"{valA} {eql}, answer:{dic[a]}")

    return dic["z"]
p=generateEquation()
print(p.count("i"))