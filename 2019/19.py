a="""109,424,203,1,21101,11,0,0,1105,1,282,21101,18,0,0,1106,0,259,2102,1,1,221,203,1,21101,0,31,0,1106,0,282,21102,38,1,0,1105,1,259,20101,0,23,2,22101,0,1,3,21101,1,0,1,21101,0,57,0,1105,1,303,2101,0,1,222,20102,1,221,3,21001,221,0,2,21101,0,259,1,21101,80,0,0,1105,1,225,21101,137,0,2,21101,91,0,0,1105,1,303,1202,1,1,223,21001,222,0,4,21102,259,1,3,21101,225,0,2,21102,225,1,1,21101,0,118,0,1106,0,225,20102,1,222,3,21101,0,88,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1106,0,259,1202,1,1,223,20102,1,221,4,20101,0,222,3,21101,24,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21101,0,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,22102,1,-3,1,22102,1,-2,2,22102,1,-1,3,21101,0,250,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,1,384,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0"""
test=""""""

def getTractor(x,y):
    inps = [x,y]
    b=[int(x) for x in a.split(",")]+[0 for _ in range(10000)]
    #print([x for x in b if x>=1000])
    i=0
    base=0
    ii = 0
    while b[i]!=99:
        jumped=False
        opcode=str(b[i])
        opcode=(5-len(opcode))*"0"+opcode
        op = int(opcode[-2:])
        #print(["","add","mul","inp","out","jm1","jm0","grt","eql","bas"][op], b[i+1:i+(4 if op in [1,2,7,8] else 3 if op in [5,6] else 2)])
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
            b[x] = inps[ii]
            ii+=1
        if op==4: 
            return x
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
size=50
total=0
for x,y in [(x,y) for y in range(size) for x in range(size)]:
    total+= getTractor(x,y)
print(total) #part 1
matrix = [[getTractor(x,y) for x in range(size)]for y in range(size)]
for y in matrix:
    print("".join([str(x) for x in y]))

def getFirstSquare(sqSize):
    x,y = (3,4)
    while True:
        print(x,y)
        isTractor = getTractor(x,y)
        if isTractor == 1:
            isTractor2 = getTractor(x+sqSize-1,y-sqSize+1)
            if isTractor2 ==1:
                return (x,y-sqSize+1)
            y+=1
        if isTractor == 0:
            x+=1
x,y = getFirstSquare(100)
print(x*10_000 + y)
#7720974 too low




