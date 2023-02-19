a="""3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99"""
test="""3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"""
test="""3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"""
test="""3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"""
#a=test
halt=False

def program(input1,input2):
    b=[int(x) for x in a.split(",")]
    #print([x for x in b if x>=1000])
    i=0
    inputIndex= 0
    inputs=[input1,input2]
    while b[i]!=99:
        jumped=False
        opcode=str(b[i])
        opcode=(5-len(opcode))*"0"+opcode
        op = int(opcode[-2:])
        _,p2,p1=[int(x) for x in opcode[:-2]]
        if op in [1,2,7,8]:
            opLength = 4
            x,y,z = b[i+1:i+opLength]
            x = x if p1 else b[x]
            y = y if p2 else b[y] 
        elif op in [5,6]:
            opLength = 3
            x,y  = b[i+1:i+opLength]
            x = x if p1 else b[x]
            y = y if p2 else b[y] 
        elif op in [3,4]:
            opLength = 2
            z = b[i+1]
            if op==4:
                z = z if p1 else b[z] 

        if op==1: b[z] = x + y
        if op==2: b[z] = x * y
        if op==3: #b[z] = input
            b[z] = inputs[inputIndex]
            inputIndex+=1
        if op==4: return z #part 1
        if op==5 and x!=0:
            jumped = True
            i=y
        if op==6 and x==0:
            jumped = True
            i=y
        if op==7: b[z] = int(x < y)
        if op==8: b[z] = int(x == y)
        if not jumped: i+=opLength
    global halt
    halt=True
    return



perms=[]
for v in range(5):
    for w in range(5):
        if w == v: continue
        for x in range(5):
            if x in [v,w]: continue
            for y in range(5):
                if y in [v,w,x]: continue
                for z in range(5):
                    if z in [v,w,x,y]: continue
                    perms.append([v,w,x,y,z])

maximum = 0
def vwxyz(v,w,x,y,z):
    q = program(v,0)
    r = program(w,q)
    s = program(x,r)
    t = program(y,s)
    u = program(z,t)
    global maximum
    if u > maximum:
        maximum = u
        print(u,"|",v,w,x,y,z,"|", q,r,s,t,u)

def bruteForce():
    for v,w,x,y,z in perms:
        vwxyz(v,w,x,y,z)
    
                
bruteForce()