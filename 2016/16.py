a="01000100010010111"
test="10000"
#a=test

def lengthen(a,l):
    la = len(a)
    while la<l:
        a = a + "0" + "".join(["1" if x=="0" else "0" for x in a[::-1]])
        la = la*2+1
    return a[:l]

def isOdd(n): return n%2!=0

def checkSum(a):
    while not isOdd(len(a)):
        a = "".join(["0" if len(set(a[i:i+2]))==2 else "1" for i in range(0,len(a),2)])
    return a

print(checkSum(lengthen(a,272)))
print(checkSum(lengthen(a,35651584)))
