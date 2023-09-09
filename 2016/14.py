a="""cuanljph"""
test="""abc"""
a=test
import hashlib
i=0
threes={}

def repeats(hash,n):
    for j in range(32-n):
        if len(set(hash[j:j+n]))==1: 
            return hash[j]
    return ""

keys=[]

while True:
    saltPlusInt = a + str(i)
    hash=hashlib.md5(saltPlusInt.encode('utf-8')).hexdigest()
    r3 = repeats(hash,3)
    if r3:
        threes[i] = r3
    r5 = repeats(hash,5)
    if r5:
        if any([x in range(i-1000,i) for x in threes]):
            keys.append(hash)
            print(i)
            
            if len(keys)==64:
                print(i)
                break
    i+= 1
    
