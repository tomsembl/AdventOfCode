a="""cuanljph"""
test="""abc"""
#a=test
import hashlib


def repeats(hash,n):
    for j in range(32-n+1):
        if len(set(hash[j:j+n]))==1: 
            return hash[j]
    return ""

def hashIt(it): return hashlib.md5(it.encode('utf-8')).hexdigest()
def hashIt2017(it): 
    for _ in range(2017):
        it = hashIt(it)
    return it


def part(p):
    i=0
    threes={}
    fives={}
    keys={}
    for i in range(32_000):
        # print(i)
        hash = hashIt(a + str(i)) if p==1 else hashIt2017(a + str(i))
        r3 = repeats(hash,3)
        if r3:
            threes[i] = r3
        r5 = repeats(hash,5)
        if r5:
            fives[i] = r5
        i+= 1
    for j in threes:
        r3=threes[j]
        for i in fives:
            r5 = fives[i]
            if i in range(j+1,j+1001) and r3==r5:
                keys[j] = hashIt(a + str(j)) if p==1 else hashIt2017(a + str(j))
                if len(keys)==70:
                    return keys
print(sorted(part(1).keys())[63])
print(sorted(part(2).keys())[63])
        
