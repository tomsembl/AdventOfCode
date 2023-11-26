def computer(inputs=[]):
    a="3,60,1005,60,18,1101,0,1,61,4,61,104,1011,104,1,1105,1,22,1101,0,0,61,3,62,1007,62,0,64,1005,64,22,3,63,1002,63,2,63,1007,63,256,65,1005,65,48,1101,0,255,61,4,61,4,62,4,63,1105,1,22,99"
    b=[int(x) for x in a.split(",")]+[0 for _ in range(10000)]
    i=0
    base=0
    output=[]

    while b[i]!=99:
        jumped=False
        opcode=str(b[i])
        opcode=(5-len(opcode))*"0"+opcode
        op = int(opcode[-2:])
        p3,p2,p1=[int(x) for x in opcode[:-2]]
        if op in [1,2,7,8]:
            opLength = 4
            x,y,z = b[i+1:i+opLength]
            if p1==2: x+=base
            if p2==2: y+=base
            if p3==2: z+=base
            x = x if p1 == 1 else b[x]
            y = y if p2 == 1 else b[y] 
        elif op in [5,6]:
            opLength = 3
            x,y  = b[i+1:i+opLength]
            if p1==2: x+=base
            if p2==2: y+=base
            x = x if p1 == 1 else b[x]
            y = y if p2 == 1 else b[y] 
        elif op in [3,4,9]:
            opLength = 2
            x = b[i+1]
            if p1==2: x+=base
            if op in [4,9]:
                x = x if p1 == 1 else b[x] 
        if op==1: b[z] = x + y
        if op==2: b[z] = x * y
        if op==3: 
            input = -1 if not inputs else inputs.pop(0)
            b[x] = input
            print("input",input)
        if op==4: 
            output.append(x)
            print(x,end="")
        if op==5 and x!=0:
            jumped = True
            i=y
        if op==6 and x==0:
            jumped = True
            i=y
        if op==7: b[z] = int(x < y)
        if op==8: b[z] = int(x == y)
        if op==9: base+=x
        if not jumped: i+=opLength
    return output
computer([1])