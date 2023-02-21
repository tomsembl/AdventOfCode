a="""3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99"""
test="3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
test="3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
#a=test

def program(inputs,ai):

    bb[ai]["inputs"]+=inputs
    while bb[ai]["b"][bb[ai]["i"]]!=99:
        jumped=False
        opcode=str(bb[ai]["b"][bb[ai]["i"]])
        opcode=(5-len(opcode))*"0"+opcode
        op = int(opcode[-2:])
        _,p2,p1=[int(x) for x in opcode[:-2]]
        if op in [1,2,7,8]:
            opLength = 4
            x,y,z = bb[ai]["b"][bb[ai]["i"]+1:bb[ai]["i"]+opLength]
            x = x if p1 else bb[ai]["b"][x]
            y = y if p2 else bb[ai]["b"][y] 
        elif op in [5,6]:
            opLength = 3
            x,y  = bb[ai]["b"][bb[ai]["i"]+1:bb[ai]["i"]+opLength]
            x = x if p1 else bb[ai]["b"][x]
            y = y if p2 else bb[ai]["b"][y] 
        elif op in [3,4]:
            opLength = 2
            z = bb[ai]["b"][bb[ai]["i"]+1]
            if op==4:
                z = z if p1 else bb[ai]["b"][z] 

        if op==1: bb[ai]["b"][z] = x + y
        if op==2: bb[ai]["b"][z] = x * y
        if op==3: 
            bb[ai]["b"][z] = bb[ai]["inputs"][bb[ai]["inputIndex"]]
            bb[ai]["inputIndex"]+=1
        if op==5 and x!=0:
            jumped = True
            bb[ai]["i"]=y
        if op==6 and x==0:
            jumped = True
            bb[ai]["i"]=y
        if op==7: bb[ai]["b"][z] = int(x < y)
        if op==8: bb[ai]["b"][z] = int(x == y)

        if not jumped: bb[ai]["i"]+=opLength
        if op==4: return z #part 1
    global halt
    halt=True
    return "halted"



perms=[]
for v in range(5,10):
    for w in range(5,10):
        if w == v: continue
        for x in range(5,10):
            if x in [v,w]: continue
            for y in range(5,10):
                if y in [v,w,x]: continue
                for z in range(5,10):
                    if z in [v,w,x,y]: continue
                    perms.append([v,w,x,y,z])

maximum = 0
maximumVars={}

def vwxyz(v,w,x,y,z):
    u=None
    global bb, halt
    halt=False
    bb={x:{"b":[int(x) for x in a.split(",")],"i":0,"inputIndex":0,"inputs":[]} for x in range(5)}
    while True:
        if halt:
            global maximum
            if u > maximum:
                maximum = u
                maximumVars[maximum] = [v,w,x,y,z]
            break
        
        if u==None:
            q = program([v,0],0)
            r = program([w,q],1)
            s = program([x,r],2)
            t = program([y,s],3)
            u = program([z,t],4)
        else:
            q = program([u],0)
            if type(q) == str: continue
            r = program([q],1)
            s = program([r],2)
            t = program([s],3)
            u = program([t],4)

def bruteForce():
    for v,w,x,y,z in perms:
        vwxyz(v,w,x,y,z)
    
                
bruteForce()
print(maximum, maximumVars[maximum])
#5483581 too low