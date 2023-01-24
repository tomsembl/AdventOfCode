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
print(sum([1 for x in a.splitlines() if any([x[:3]=="mul" and x[-2:]==" 1",x[:3]=="add" and x[-2:]==" 0",x[:3]=="div" and x[-2:]==" 1"])]))
instr=[[int(y) if y.isnumeric() or "-" in y else y for y in x.split()]+([-1] if x[0]=="i" else []) for x in a.splitlines() if x[0]!="#"]
instr=[[ops.index(op),"wxyz".index(a),c:=type(b)==int,b if c else "wxyz".index(b)] for op,a,b in instr]
def runForward(input,outputDic=False):
    dic={0:0,1:0,2:0,3:0}
    i=0
    for x in instr: 
        # try:
        #print(x)
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
        # except:
        #     print("lose",i,x)
        #     break
    #print(input,list(dic.values()))
    if outputDic: return dic
    return dic[3]

lowest=12395412163313
#12395412163313
#12373567167723
def randomMethod1():
    from random import randint
    global lowest
    while True:
        # string=""
        # for x in range(14): string+=str(randint(1,9))
        string=str(randint(11111111111111,99999999999999))
        if "0" in string: continue
        if string[-3]!=string[-4]: continue
        if string[0]!="1": continue
        try:
            answer = runForward(string)
            if answer < lowest:
                lowest=answer
                print(F"{string} win {answer}")
        except: pass
#randomMethod1()

def scrambleMethod1():
    global lowest
    initial="12395412163313"

    for i in range(14): 
        print("\ni:",i)
        for j in range(1,10): 
            string=initial[:i]+str(j)+initial[i+1:]
            try:
                answer = runForward(string)
                if answer < lowest:
                    lowest=answer
                    print(F"{string} win {answer}")
                print(string,answer)
            except: pass
#scrambleMethod1()

def scrambleMethod2():
    from random import randint
    global lowest
    initial="12395412163313"
    seen=[initial]
    for i in range(2,15):#number of digits to change

        print("\ni:",i)
        countSinceWin=0
        while countSinceWin<100000: #number of tries
            string=initial
            positsToChange=[]
            for _ in range(i): #loop on positions to change
                while True:
                    ii=randint(0,13)
                    if ii not in positsToChange: break
                positsToChange.append(randint(0,13))
            for ii in positsToChange:
                string=string[:ii]+str(randint(1,9))+string[ii+1:]

            answer = runForward(string)
            countSinceWin+=1
            if answer == lowest and string not in seen: 
                countSinceWin=0
                seen.append(string)
                print(F"{string} win {answer}")
            if answer < lowest:
                lowest=answer
                print(F"{string} win {answer}")
            #print(string,answer)
    freq={x:{y:0 for y in range(1,10)} for x in range(14)}
    for s in seen:
        for i in range(14):
            freq[i][int(s[i])]+=1
    for i in freq:
        print("\ni:",i)
        for x in freq[i]:
            print(x,"count:",freq[i][x])

#scrambleMethod2()

def inputMethod():
    while True:
        try:
            x=runForward(input("input:"),True)
            print(F"win {x}")
        except: pass
inputMethod()
45295867270056
49814645545579

# 0: [a, 1, 9+a, 9+a]
# 1: [b, 1, 4+b, 24*ab+b]