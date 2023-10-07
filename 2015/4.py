import hashlib

a="""iwrupvqb"""
test="""abcdef"""
#a=test
def part(p):
    for x in range(1_000_000_000):
        key = a+str(x)
        hash=hashlib.md5(key.encode('utf-8')).hexdigest()
        zeroLength = 5 if p==1 else 6
        if hash[:zeroLength]=="0"*zeroLength:
            print(x)
            break
part(1)
part(2)